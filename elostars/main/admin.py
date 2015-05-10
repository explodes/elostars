from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

from elostars.lib import admin as a
from elostars.main import models as main


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = main.User

    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)


class MyUserAddForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = main.User

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
        "gender",
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
        "gender",
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
        (_("Personal info"), {"fields": (
            "first_name",
            "last_name",
            "gender",
            "view_gender",
        )}),
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
                "last_name",
                "gender",
                "view_gender",
            ),
        }),
    )


class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        a.thumb('image'),
        a.thumb('image_128x128'),
        "active",
        "wins",
        "losses",
        "score",
        "supposed_gender",
    )
    search_fields = ("user__first_name", "user__last_name", "user__username",)
    list_filter = (
        "active",
        "user__gender",
    )
    list_select_related = True

    raw_id_fields = ("user",)
    readonly_fields = ("_image_128x128",)


admin.site.register(main.User, MyUserAdmin)
admin.site.register(main.Picture, PictureAdmin)