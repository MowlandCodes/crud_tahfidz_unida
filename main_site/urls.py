from django.urls import path, re_path

from . import views

# View Routes
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("hafalan", views.hafalan, name="hafalan"),
    path("login", views.login_page, name="login_page"),
    path("logout", views.logout_view, name="logout_view"),
    path("forgot-password", views.forgot_password, name="forgot_password"),
    path("send-email/<str:email>", views.send_reset_link, name="reset_link"),
    path("reset-password/<uuid:uuid>", views.reset_password, name="reset_password"),
    re_path("^admin/login/$", views.admin_login, name="admin_login"),
]
