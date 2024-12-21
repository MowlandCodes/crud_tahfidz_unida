from django.urls import path

from . import views

# View Routes
urlpatterns = [
    path("", views.index, name="Index Page"),
]
