from django import forms

from elostars.lib import matchup
from elostars.main import models as main


class SignupForm(forms.ModelForm):
    password = forms.CharField(required=True, min_length=8,
        widget=forms.PasswordInput())
    picture = forms.ImageField(required=True)

    class Meta:
        model = main.User
        fields = ("username", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)

        password = self.cleaned_data["password"]
        user.set_password(password)

        if commit:
            user.save()
            image = self.cleaned_data["picture"]
            picture = main.Picture(user=user, image=image)
            picture.save()

        return user


class MatchupForm(forms.Form):
    key = forms.CharField(required=True, widget=forms.HiddenInput())
    winner = forms.CharField(required=True, widget=forms.HiddenInput())

    def clean_key(self):
        key = self.cleaned_data["key"]

        if not matchup.validate_matchup(key):
            print "INVALID MATCHUP"
            raise forms.ValidationError("Invalid matchup")

        print "VALID MATCHUP"

        return key

    def clean(self):
        cleaned_data = self.cleaned_data

        key = cleaned_data.get("key")
        winner = cleaned_data.get("winner")

        print self.data
        print cleaned_data

        if key and winner:
            pair = matchup.get_matchup(key)

            if winner == pair.left.guid:
                cleaned_data["winner"] = pair.left
                cleaned_data["loser"] = pair.right
            elif winner == pair.right.guid:
                cleaned_data["winner"] = pair.right
                cleaned_data["loser"] = pair.left
            else:
                raise forms.ValidationError("Invalid winner")

            cleaned_data["pair"] = pair
        else:
            raise forms.ValidationError("Invalid rating")

        return cleaned_data

