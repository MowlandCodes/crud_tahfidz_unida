from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignupForm, SetoranHafalan

# Create your views here.
def index(response):
    return redirect("dashboard")

def dashboard(response):
    return render(response, "main_site/dashboard.html", {})

def login(response):
    return render(response, "main_site/login.html", {})

def signup(response):
    return render(response, "main_site/signup.html", {})
