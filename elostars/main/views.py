from django import http
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import decorators as auth
from django.contrib.auth import login
from django.core import exceptions as e
from django.shortcuts import render, redirect

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

    from elostars.lib.guid import make_guid

    form = forms.SignupForm(request.POST or None, request.FILES or None,
        initial={} if not settings.DEBUG else {
            "username": "test-%s" % make_guid()[:4],
            "email": "%s@example.com" % make_guid()[:6],
            "first_name": "Cheesey",
            "last_name": "McNasty",
            "password": "superpad",

        })
    if form.is_valid():
        user = form.save()
        user = authenticate(
            username=user.username,
            password=request.POST["password"]
        )
        login(request, user)
        return redirect("main:rate")
    return render(request, template, {
        "form": form
    })


@auth.login_required(login_url="main:home")
def rate(request, template="rate.html"):
    old_pair = None
    if request.method == "POST":
        key = request.POST.get("key")
        form = forms.MatchupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            winner = data["winner"]
            loser = data["loser"]
            # todo: save rating
            winner.win_against(loser)
            old_pair = data["pair"]
        matchup.close_matchup(key)

    pair = matchup.create_matchup(request.user)

    if pair is None:
        form = None
    else:
        form = forms.MatchupForm(initial={"key": pair.key})

    if old_pair:
        if old_pair.right.score > old_pair.left.score:
            old_pair = matchup.Matchup(
                old_pair.key, old_pair.right, old_pair.left)

    return render(request, template, {
        "form": form,
        "pair": pair,
        "old_pair": old_pair,
    })


@auth.login_required(login_url="main:home")
def user_settings(request, template="settings.html"):
    if request.method == "POST":
        action = request.POST.get("action", None)
        if action == "settings":
            settings_form = forms.SettingsForm(request.POST,
                instance=request.user)
            if settings_form.is_valid():
                settings_form.save()
                return redirect("main:settings")
        else:
            guid = request.POST.get("guid", None)
            try:
                picture = main.Picture.objects.get(guid=guid, user=request.user)
            except e.ObjectDoesNotExist:
                raise http.Http404()
            else:
                if action == "activate":
                    picture.active = True
                    picture.save()
                elif action == "deactivate":
                    picture.active = False
                    picture.save()
                elif action == "delete":
                    picture.delete()
                return redirect("main:settings")
    else:
        settings_form = forms.SettingsForm(instance=request.user)

    pictures = request.user.pictures.all()

    return render(request, template, {
        "pictures": pictures,
        "settings_form": settings_form
    })


def privacy(request, template="privacy.html"):
    return render(request, template, {
    })


def terms(request, template="terms.html"):
    return render(request, template, {
    })