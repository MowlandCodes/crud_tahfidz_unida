from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hafalan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hafalan")
    surat = models.CharField(max_length=75)
    ayat_start = models.IntegerField(default=0)
    ayat_end = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ------------> {self.surat} : {self.ayat_start} - {self.ayat_end}"
