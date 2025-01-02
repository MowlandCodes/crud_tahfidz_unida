from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hafalan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hafalan")
    surat = models.CharField(max_length=75)
    ayat_start = models.IntegerField(default=0)
    ayat_end = models.IntegerField(default=1) 
    date = models.DateTimeField(blank=True, null=True)

    def total_ayat(self):
        return self.ayat_end - self.ayat_start

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ------------> {self.surat} : {self.ayat_start} - {self.ayat_end}"
