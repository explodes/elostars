from django.shortcuts import render, redirect
from django.contrib.auth import decorators as auth
from django.contrib.auth import login

from elostars.lib import matchup
from elostars.main import forms
from elostars.main import models as main


def home(request, template="home.html"):
    users = main.User.objects.order_by("first_name").all()
    return render(request, template, {
        "users": users
    })


def signup(request, template="registration/signup.html"):
    if request.user.is_authenticated():
        return redirect("main:rate")
    form = forms.SignupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("main:rate")
    return render(request, template, {
        "form": form
    })


#@auth.login_required(login_url="main:home")
def rate(request, template="rate.html"):

    if request.method == "POST":
        key = request.POST.get("key")
        form = forms.MatchupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            winner = data["winner"]
            loser = data["loser"]
            # todo: save rating
            return redirect("main:rate")
        matchup.close_matchup(key)

    pair = matchup.create_matchup(request.user.pk)
    form = forms.MatchupForm(initial={"key": pair.key})

    return render(request, template, {
        "form": form,
        "pair": pair,
    })


@auth.login_required(login_url="main:home")
def settings(request, template="settings.html"):
    return render(request, template, {

    })