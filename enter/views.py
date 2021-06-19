from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate
from django.db import IntegrityError


def login(request):
    if request.method == "POST":
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard/")
        else:
            messages.error(request, "Ops! Dados inválidos. 😢")
            return render(request, "index_login.html")
    else:
        return render(request, "index_login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
