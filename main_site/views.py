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

def admin_login(request): # Redirecting to login page
    return redirect("/login")

def dashboard(request):
    if request.user.is_authenticated and not (request.user.is_staff or request.user.is_superuser): # Allow only authenticated user to access dashboard and Not admin or staff
        return render(request, "main_site/dashboard.html", {})
    
    elif request.user.is_staff or request.user.is_superuser: # Preventing admin to touch user Dashboard page
        return redirect("/admin")

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
            if request.user.is_staff: # Check if user is a staff or a Super User
                return redirect("/admin")
            else:
                if remember == "True": # If remember is checked, set remember to True
                    request.session.set_expiry(60 * 60 * 24 * 7 * 2) # Will remember the user for 2 weeks
                else:
                    request.session.set_expiry(0) # Expire when the browser is closed

                return redirect("/dashboard") # Page for Students
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
