from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, SignupForm, SetoranHafalan

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello World, You're at the main page</h1>")

def dashboard(response):
    return render(response, "main_site/dashboard.html", {})

def login(response):
    return render(response, "main_site/login.html", {})

def signup(response):
    return render(response, "main_site/signup.html", {})
