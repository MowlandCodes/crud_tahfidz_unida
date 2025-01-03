import calendar
import datetime
import json  # To dump data into json format
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Case, F, Q, Sum, Value, When
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django_ratelimit.decorators import ratelimit

# Import the database model to display on the dashboard
from .models import Hafalan


# Create your views here.
def index(request):
    return redirect("/login")


def admin_login(request):  # Redirecting to login page
    return redirect("/login")


def dashboard(request):
    if request.user.is_authenticated and not (
        request.user.is_staff or request.user.is_superuser
    ):  # Allow only authenticated user to access dashboard and Not admin or staff

        current_user = request.user

        now = datetime.now()
        current_month = now.month
        current_year = now.year
        previous_month = (now - timedelta(days=30)).month
        previous_year = (now - timedelta(days=30)).year

        weeks = [f"Week-{i}" for i in range(1, 6)]

        current_data = {week: 0 for week in weeks}
        previous_data = {week: 0 for week in weeks}

        # Defining the current User's Quran memorization
        hafalan_user = Hafalan.objects.filter(user=current_user)

        hafalan_data_mingguan = (
            hafalan_user.annotate(
                day=F("date__day"),
                week=Case(
                    When(day__range=(1, 7), then=Value("Week-1")),
                    When(day__range=(8, 14), then=Value("Week-2")),
                    When(day__range=(15, 21), then=Value("Week-3")),
                    When(day__range=(22, 28), then=Value("Week-4")),
                    default=Value("Week-5"),
                ),
                month=F("date__month"),
                year=F("date__year"),
            )
            .filter(
                (
                    Q(month=current_month, year=current_year)
                    | Q(month=previous_month, year=previous_year)
                )
            )
            .values("week", "month", "year")
            .annotate(total_memorized=Sum("ayat_end") - Sum("ayat_start") + Sum(1))
            .order_by("month", "week")
        )


        for entry in hafalan_data_mingguan:
            week = entry["week"]
            total_memorized = entry["total_memorized"]
            month = entry["month"]
            year = entry["year"]
            if month == current_month and year == current_year:
                current_data[week] = total_memorized
            elif month == previous_month and year == previous_year:
                previous_data[week] = total_memorized

        chart_data = {
            "labels": weeks,
            "datasets": [
                {
                    "label": calendar.month_name[current_month]
                    + " - "
                    + str(current_year),
                    "data": [current_data[week] for week in weeks],
                    "backgroundColor": "rgba(75, 192, 192, 0.8)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 2,
                },
                {
                    "label": calendar.month_name[previous_month]
                    + " - "
                    + str(previous_year),
                    "data": [previous_data[week] for week in weeks],
                    "backgroundColor": "rgba(255, 99, 132, 0.8)",
                    "borderColor": "rgba(255, 99, 132, 1)",
                    "borderWidth": 2,
                },
            ],
        }

        return render(
            request,
            "main_site/dashboard.html",
            {"chart_data": chart_data},
        )

    elif (
        request.user.is_staff or request.user.is_superuser
    ):  # Preventing admin to touch user Dashboard page
        return redirect("/admin")

    else:
        return redirect("/login")


# Limiting login attempts to prevent Brute Force Attack
@ratelimit(key="user_or_ip", rate="7/m", block=True)
def login_page(request):
    csrf_token = get_token(request)
    if (
        request.user.is_authenticated
    ):  # Preventing the user to touch login page after successfully logged in
        return redirect("/dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        remember = request.POST.get("remember", False)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:  # Check if user is a staff or a Super User
                return redirect("/admin")
            else:
                if remember == "True":  # If remember is checked, set remember to True
                    request.session.set_expiry(
                        60 * 60 * 24 * 7 * 2
                    )  # Will remember the user for 2 weeks
                else:
                    request.session.set_expiry(0)  # Expire when the browser is closed

                return redirect("/dashboard")  # Page for Students
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "main_site/login.html", {"csrf_token": csrf_token})


def signup(request):
    return render(request, "main_site/signup.html", {})


def hafalan(request):
    return render(request, "main_site/crud_hafalan.html", {})


def logout_view(request):
    logout(request)
    return redirect("/login")
