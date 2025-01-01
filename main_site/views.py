from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    return redirect("login")

def dashboard(request):
    return render(request, "main_site/dashboard.html", {})

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        remember = request.POST.get("remember", False)

        return HttpResponse(f"Username : {username} <br> Password : {password} <br> Remember : {remember}")

    else:
        return render(request, "main_site/login.html", {})

def signup(request):
    return render(request, "main_site/signup.html", {})
