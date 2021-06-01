from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def errorlog(request):
    messages.info(request, "Please login to view the content")
    return redirect("/")


def index(request):

    return render(request, "index.html",)
