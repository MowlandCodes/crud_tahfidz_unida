import calendar
import datetime
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Case, F, Q, Sum, Value, When
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django_ratelimit.decorators import ratelimit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
from email.utils import formataddr

# Import the database model to display on the dashboard
from .models import Hafalan, PasswordResetToken


# Create your views here.
def index(_):
    return redirect("login_page")


def admin_login(_):  # Redirecting to login page
    return redirect("login_page")


@login_required
def dashboard(request):
    if request.user.is_authenticated and not ( request.user.is_staff or request.user.is_superuser ):  # Allow only authenticated user to access dashboard and Not admin or staff
        current_user = request.user

        now = datetime.now()
        current_month = now.month
        current_year = now.year
        previous_month = (now - timedelta(days=30)).month
        previous_year = (now - timedelta(days=30)).year

        weeks = [f"Week-{i}" for i in range(1, 6)]
        months = [f"{datetime(current_year, i, 1).strftime('%B')}" for i in range(1, 13)]
        monthly_data = {month : 0 for month in months}

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

        hafalan_data_tahunan = (
            hafalan_user.filter(
                date__year=current_year
            ).annotate(
                month=F('date__month')
            ).values('month').annotate(
                total_memorized=Sum('ayat_end') - Sum('ayat_start') + Sum(1)
            ).order_by('month')
        )

        for entry in hafalan_data_tahunan:
            month_name = datetime(current_year, entry['month'], 1).strftime('%B')
            monthly_data[month_name] = entry['total_memorized']


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

        chart_data_tahunan = {
            'labels': months,
            'datasets': [
                {
                    'label': 'Jumlah Setoran (ayat)',
                    'data': list(monthly_data.values()),
                    'backgroundColor': 'rgba(75, 192, 192, 0.8)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderWidth': 2
                }
            ]
        }

        return render(
            request,
            "main_site/dashboard.html",
            {"chart_data": chart_data, "chart_data_tahunan": chart_data_tahunan},
        )

    elif request.user.is_authenticated and ( request.user.is_staff or request.user.is_superuser ):  # Preventing admin to touch user Dashboard page
        return redirect("/admin")

    else:
        return redirect("login_page")


# Limiting login attempts to prevent Brute Force Attack
@ratelimit(key="user_or_ip", rate="7/m", block=True)
def login_page(request):
    csrf_token = get_token(request)
    if request.user.is_authenticated:  # Preventing the user to touch login page after successfully logged in
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        remember = request.POST.get("remember", False)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:  # Check if user is a staff or a Super User
                return redirect("admin_login")
            else:
                if remember == "True":  # If remember is checked, set remember to True
                    request.session.set_expiry(
                        60 * 60 * 24 * 7 * 2
                    )  # Will remember the user for 2 weeks
                else:
                    request.session.set_expiry(0)  # Expire when the browser is closed

                return redirect("dashboard")  # Page for Students
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "main_site/login.html", {"csrf_token": csrf_token})


@login_required
def hafalan(request):
    if request.user.is_authenticated and not (request.user.is_staff or request.user.is_superuser): # To ensure that the Staff user can't access the student's page
        current_user = request.user
        
        hafalan_user = Hafalan.objects.filter(user=current_user).order_by('-date')

        return render(request, "main_site/hafalan.html", { 'hafalan_data' : hafalan_user })

    elif request.user.is_staff or request.user.is_superuser:
        return redirect("admin_login")

    else:
        return redirect("login_page")

def logout_view(request):
    logout(request)
    return redirect("login_page")

def send_reset_link(request, email):
    try:
        current_user = User.objects.get(email=email)
        reset_request, is_created = PasswordResetToken.objects.get_or_create(user=current_user)
        if is_created:
            reset_request.save()

        reset_link = f"{request.scheme}://{request.get_host()}/reset-password/{reset_request.token}/{current_user.uuid}"
        sender = formataddr(("Staff Tahfidz UNIDA", "tahfidz@unida.gontor.ac.id"))
        
        email_content = EmailMessage(
            subject="Reset Password",
            body=f"Click the link below to reset your password: {reset_link}",
            from_email=sender,
            to=[current_user.email],
        )

        email_content.send()
        messages.success(request, "Reset password link has been sent to your email address")
        return redirect("login_page")

    except (User.DoesNotExist, Exception):
        messages.error(request, "Error on creating reset password link")
        return redirect("login_page")

def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            _ = User.objects.get(email=email)
            link = reverse("reset_link", kwargs={"email": email})
            return redirect(link)
        except Exception:
            messages.error(request, "User with this email address does not exist")
            return redirect("forgot_password")

    return render(request, "main_site/forgot-password.html", {})


def reset_password(request, token, uuid):
    try:
        current_user = User.objects.get(uuid=uuid)
        reset_request = PasswordResetToken.objects.get(user=current_user, token=token, expires_at__gte=datetime.now())

    except (User.DoesNotExist, PasswordResetToken.DoesNotExist, Exception):
        messages.error(request, "Invalid token or expired token")
        return redirect("login_page")

    if request.method == "POST":
        new_password = request.POST["password"]
        confirm_password = request.POST["password_confirm"]

        if new_password == confirm_password:
            user = User.objects.get(uuid=uuid)
            user.set_password(new_password)
            user.save()
            reset_request.delete() # Delete the reset token
            messages.success(request, "Password has been reset successfully")
            return redirect("login_page")
        else:
            messages.error(request, "Password and confirm password do not match")

    else:
        return render(request, "main_site/reset-password.html", {"token": token, "uuid": uuid})
