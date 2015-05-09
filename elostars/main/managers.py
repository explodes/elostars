from django.contrib.auth.models import BaseUserManager

from elostars.lib import managers as m


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, is_active=True, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class PictureManager(m.QuerySetManager):
    class QuerySet(m.QuerySet):
        def active(self):
            return self.filter(active=True)

        def matchup(self, from_user, exclude=None):

            q = self.active()

            if from_user.view_gender != "both":
                q = q.filter(user__gender=from_user.view_gender)

            q = q.exclude(pk=from_user.pk)

            if exclude is not None:
                q = q.exclude(pk=exclude.pk)

            return q.order_by('?')
