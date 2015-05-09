from django import forms

from elostars.main import models as main


class SignupForm(forms.ModelForm):
    picture = forms.ImageField(required=True)

    class Meta:
        model = main.User
        fields = ("username", "email", "first_name", "last_name", "password")