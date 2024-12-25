from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello World, You're at the main page</h1>")

def dasboard(response):
    return render(response, "main_site/dashboard.html", {})
