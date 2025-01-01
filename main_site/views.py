from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.middleware.csrf import get_token
from django_ratelimit.decorators import ratelimit

# Create your views here.
def index(request):
    return redirect("/login")

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "main_site/dashboard.html", {})
    else:
        return redirect("/login")

# Limiting login attempts to prevent Brute Force Attack
@ratelimit(key='user_or_ip', rate='7/m', block=True)
def login_page(request):
    csrf_token = get_token(request)
    if request.user.is_authenticated: # Preventing the user to touch login page after successfully logged in
        return redirect("/dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        remember = request.POST.get("remember", False)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "main_site/login.html", {"csrf_token" : csrf_token})

def signup(request):
    return render(request, "main_site/signup.html", {})

def hafalan(request):
    return render(request, "main_site/crud_hafalan.html", {})

def logout_view(request):
    logout(request)
    return redirect("/login")
