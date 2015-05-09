from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

from elostars.main.models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)


class MyUserAddForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(MyUserAddForm, self).__init__(*args, **kwargs)


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserAddForm

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
    )
    ordering = (
        "username",
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Permissions"), {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
        )}),
        (_("Personal info"),
         {"fields": ("first_name", "last_name")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_superuser",
                "first_name",
                "last_name",),
        }),
    )


admin.site.register(User, MyUserAdmin)