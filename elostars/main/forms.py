from django import forms

from elostars.lib import matchup
from elostars.main import models as main


class SignupForm(forms.ModelForm):
    picture = forms.ImageField(required=True)

    class Meta:
        model = main.User
        fields = ("username", "email", "first_name", "last_name", "password")


class MatchupForm(forms.Form):
    key = forms.HiddenInput()
    winner = forms.HiddenInput()

    def clean_key(self):
        key = self.cleaned_data["key"]

        if not matchup.validate_matchup(key):
            raise forms.ValidationError("Invalid matchup")

        return key

    def clean(self):

        data = self.cleaned_data

        key = data.get("key")
        winner = data.get("winner")

        if key and winner:
            pair = matchup.get_matchup(key)

            if winner == pair.left.guid:
                data["winner"] = pair.left
                data["loser"] = pair.right
            elif winner == pair.right.guid:
                data["winner"] = pair.right
                data["loser"] = pair.left
            else:
                raise forms.ValidationError("Invalid winner")

            data["pair"] = pair

        return data

