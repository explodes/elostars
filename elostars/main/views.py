from django.shortcuts import render

from elostars.main import models as main


def home(request, template="home.html"):

    users = main.User.objects.order_by("first_name").all()

    return render(request, template, {
        "users": users
    })


