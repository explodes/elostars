import binascii

import os
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from elostars.lib import models as m
from elostars.main import managers


def make_guid():
    return binascii.b2a_hex(os.urandom(64))


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

    image = models.ImageField(_(u"image"),
                              upload_to="images", null=True, blank=True)
    _image_128x128 = models.CharField(_(u"image 128x128"), max_length=1024,
                                      null=True, blank=True)

    active = models.BooleanField(default=True)

    objects = managers.PictureManager()

    class Meta:
        app_label = "main"
        verbose_name = _(u"picture")
        verbose_name_plural = _(u"pictures")

    def __unicode__(self):
        return self.name

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