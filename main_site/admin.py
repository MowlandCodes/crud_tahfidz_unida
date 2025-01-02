from django.contrib import admin
from django.utils.translation import gettext_lazy as text
from django import forms
from django.contrib.auth.models import User

from .models import Hafalan

class HafalanForm(forms.ModelForm):
    class Meta:
        model = Hafalan
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.filter(is_superuser=False, is_staff=False)
        self.fields["user"].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"

# Register your models here.
@admin.register(Hafalan)
class HafalanAdmin(admin.ModelAdmin):
    form = HafalanForm
    list_display = ["name", "surat", "ayat_start", "ayat_end", "date"]

    def name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    name.short_description = "Full Name"

# Change the admin site header, title, and index title
admin.site.site_header = text("Tahfidz CRUD Dashboard")
admin.site.site_title = text("Tahfidz CRUD")
admin.site.index_title = text("Tahfidz CRUD Dashboard")
