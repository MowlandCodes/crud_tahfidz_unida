from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=150)
    username = models.CharField(max_length=75, default="")
    email = models.EmailField()
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Hafalan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    surat = models.CharField(max_length=75)
    ayat = models.IntegerField()

    def __str__(self):
        return f"{self.surat} : {self.ayat}"
