from django.contrib import admin
from django.utils.translation import gettext_lazy as text

from .models import Hafalan

# Register your models here.
admin.site.register(Hafalan)

# Change the admin site header, title, and index title
admin.site.site_header = text("Tahfidz CRUD Dashboard")
admin.site.site_title = text("Tahfidz CRUD")
admin.site.index_title = text("Tahfidz CRUD Dashboard")
