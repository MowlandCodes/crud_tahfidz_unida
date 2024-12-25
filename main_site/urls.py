from django.urls import path

from . import views

# View Routes
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]
