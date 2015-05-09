from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from elostars.main import managers


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    username = models.CharField(_("username"), max_length=128, unique=True)
    email = models.EmailField(_("email"), max_length=128, unique=True)

    first_name = models.CharField(_("first name"), max_length=128, null=True,
                                  blank=True)
    last_name = models.CharField(_("last name"), max_length=128, null=True,
                                 blank=True)
    is_active = models.BooleanField(_("active"), default=True, help_text=_(
        "Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts."))

    is_staff = models.BooleanField(_("is admin"), default=False)

    date_joined = models.DateTimeField(_("created at"), auto_now_add=True)

    objects = managers.UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("email",)

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
