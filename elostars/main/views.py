from django.shortcuts import render, redirect
from django.contrib.auth import decorators as auth
from django.contrib.auth import login

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


@auth.login_required(login_url="main:home")
def rate(request, template="rate.html"):
    return render(request, template, {

    })


def settings(request, template="settings.html"):
    return render(request, template, {

    })