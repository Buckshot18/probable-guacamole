from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BandMember, Event

def home(request):
    return render(request, "band_app/home.html")

def band_members(request):
    members = BandMember.objects.all()
    return render(request, "band_app/members.html", {"members": members})

def events(request):
    events = Event.objects.all()
    return render(request, "band_app/events.html", {"events": events})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "band_app/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "band_app/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("home")
