from __future__ import division

import math

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from elostars.lib import models as m
from elostars.lib.guid import make_guid
from elostars.main import managers


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    username = models.CharField(_("username"), max_length=128, unique=True)
    email = models.EmailField(_("email"), max_length=128, unique=True)

    guid = models.CharField(_("guid"), max_length=128, unique=True,
        default=make_guid)

    first_name = models.CharField(_("first name"), max_length=128)
    last_name = models.CharField(_("last name"), max_length=128)
    is_active = models.BooleanField(_("active"), default=True, help_text=_(
        "Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts."))

    is_staff = models.BooleanField(_("is admin"), default=False)

    date_joined = models.DateTimeField(_("created at"), auto_now_add=True)

    objects = managers.UserManager()

    class Meta:
        app_label = "main"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("email",)

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name


class Picture(m.AutoImageSizingModel):
    user = models.ForeignKey(User)

    guid = models.CharField(_("guid"), max_length=128, unique=True,
        default=make_guid)

    image = models.ImageField(_(u"image"),
        upload_to="images", null=True, blank=True)
    _image_128x128 = models.CharField(_(u"image 128x128"), max_length=1024,
        null=True, blank=True)

    active = models.BooleanField(default=True)

    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=1600)

    objects = managers.PictureManager()

    class Meta:
        app_label = "main"
        verbose_name = _(u"picture")
        verbose_name_plural = _(u"pictures")

    def __unicode__(self):
        return unicode(self.user)

    def image_sizes(self):
        return (
            ("_image_128x128", (128, 128)),
        )

    def upload_to(self):
        return "images"

    @property
    def image_128x128(self):
        if self._image_128x128:
            return settings.MEDIA_URL + self._image_128x128

    def win_against(self, loser):
        rating_winner = self.score
        rating_loser = loser.score

        score_winner = 1
        score_loser = 0

        estimate_winner = 1 / (1 + 10 ** ((rating_loser - rating_winner) / 400))
        estimate_loser = 1 / (1 + 10 ** ((rating_winner - rating_loser) / 400))

        rating_winner += int(math.ceil(32 * (score_winner - estimate_winner)))
        rating_loser += int(math.ceil(32 * (score_loser - estimate_loser)))

        self.wins += 1
        self.score = rating_winner

        loser.losses += 1
        loser.score = rating_loser

        self.save()
        loser.save()
