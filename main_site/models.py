from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models

import secrets

# Create your models here.
SURAHS = [
    ("Al-Faatiha", "Al-Faatiha"),
    ("Al-Baqara", "Al-Baqara"),
    ("Aal-i-Imraan", "Aal-i-Imraan"),
    ("An-Nisaa", "An-Nisaa"),
    ("Al-Maaida", "Al-Maaida"),
    ("Al-An'aam", "Al-An'aam"),
    ("Al-A'raaf", "Al-A'raaf"),
    ("Al-Anfaal", "Al-Anfaal"),
    ("At-Tawba", "At-Tawba"),
    ("Yunus", "Yunus"),
    ("Hud", "Hud"),
    ("Yusuf", "Yusuf"),
    ("Ar-Ra'd", "Ar-Ra'd"),
    ("Ibrahim", "Ibrahim"),
    ("Al-Hijr", "Al-Hijr"),
    ("An-Nahl", "An-Nahl"),
    ("Al-Israa", "Al-Israa"),
    ("Al-Kahf", "Al-Kahf"),
    ("Maryam", "Maryam"),
    ("Taa-Haa", "Taa-Haa"),
    ("Al-Anbiyaa", "Al-Anbiyaa"),
    ("Al-Hajj", "Al-Hajj"),
    ("Al-Muminoon", "Al-Muminoon"),
    ("An-Noor", "An-Noor"),
    ("Al-Furqaan", "Al-Furqaan"),
    ("Ash-Shu'araa", "Ash-Shu'araa"),
    ("An-Naml", "An-Naml"),
    ("Al-Qasas", "Al-Qasas"),
    ("Al-Ankaboot", "Al-Ankaboot"),
    ("Ar-Room", "Ar-Room"),
    ("Luqman", "Luqman"),
    ("As-Sajda", "As-Sajda"),
    ("Al-Ahzaab", "Al-Ahzaab"),
    ("Saba", "Saba"),
    ("Faatir", "Faatir"),
    ("Yaseen", "Yaseen"),
    ("As-Saaffaat", "As-Saaffaat"),
    ("Saad", "Saad"),
    ("Az-Zumar", "Az-Zumar"),
    ("Ghafir", "Ghafir"),
    ("Fussilat", "Fussilat"),
    ("Ash-Shura", "Ash-Shura"),
    ("Az-Zukhruf", "Az-Zukhruf"),
    ("Ad-Dukhaan", "Ad-Dukhaan"),
    ("Al-Jaathiya", "Al-Jaathiya"),
    ("Al-Ahqaf", "Al-Ahqaf"),
    ("Muhammad", "Muhammad"),
    ("Al-Fath", "Al-Fath"),
    ("Al-Hujuraat", "Al-Hujuraat"),
    ("Qaaf", "Qaaf"),
    ("Adh-Dhaariyat", "Adh-Dhaariyat"),
    ("At-Tur", "At-Tur"),
    ("An-Najm", "An-Najm"),
    ("Al-Qamar", "Al-Qamar"),
    ("Ar-Rahmaan", "Ar-Rahmaan"),
    ("Al-Waaqia", "Al-Waaqia"),
    ("Al-Hadid", "Al-Hadid"),
    ("Al-Mujaadila", "Al-Mujaadila"),
    ("Al-Hashr", "Al-Hashr"),
    ("Al-Mumtahana", "Al-Mumtahana"),
    ("As-Saff", "As-Saff"),
    ("Al-Jumu'a", "Al-Jumu'a"),
    ("Al-Munaafiqoon", "Al-Munaafiqoon"),
    ("At-Taghaabun", "At-Taghaabun"),
    ("At-Talaaq", "At-Talaaq"),
    ("At-Tahrim", "At-Tahrim"),
    ("Al-Mulk", "Al-Mulk"),
    ("Al-Qalam", "Al-Qalam"),
    ("Al-Haaqqa", "Al-Haaqqa"),
    ("Al-Ma'aarij", "Al-Ma'aarij"),
    ("Nooh", "Nooh"),
    ("Al-Jinn", "Al-Jinn"),
    ("Al-Muzzammil", "Al-Muzzammil"),
    ("Al-Muddaththir", "Al-Muddaththir"),
    ("Al-Qiyaama", "Al-Qiyaama"),
    ("Al-Insaan", "Al-Insaan"),
    ("Al-Mursalaat", "Al-Mursalaat"),
    ("An-Naba", "An-Naba"),
    ("An-Naazi'aat", "An-Naazi'aat"),
    ("Abasa", "Abasa"),
    ("At-Takwir", "At-Takwir"),
    ("Al-Infitaar", "Al-Infitaar"),
    ("Al-Mutaffifin", "Al-Mutaffifin"),
    ("Al-Inshiqaaq", "Al-Inshiqaaq"),
    ("Al-Burooj", "Al-Burooj"),
    ("At-Taariq", "At-Taariq"),
    ("Al-A'laa", "Al-A'laa"),
    ("Al-Ghaashiya", "Al-Ghaashiya"),
    ("Al-Fajr", "Al-Fajr"),
    ("Al-Balad", "Al-Balad"),
    ("Ash-Shams", "Ash-Shams"),
    ("Al-Lail", "Al-Lail"),
    ("Ad-Dhuhaa", "Ad-Dhuhaa"),
    ("Ash-Sharh", "Ash-Sharh"),
    ("At-Tin", "At-Tin"),
    ("Al-Alaq", "Al-Alaq"),
    ("Al-Qadr", "Al-Qadr"),
    ("Al-Bayyina", "Al-Bayyina"),
    ("Az-Zalzala", "Az-Zalzala"),
    ("Al-Aadiyaat", "Al-Aadiyaat"),
    ("Al-Qaari'a", "Al-Qaari'a"),
    ("At-Takaathur", "At-Takaathur"),
    ("Al-Asr", "Al-Asr"),
    ("Al-Humaza", "Al-Humaza"),
    ("Al-Fil", "Al-Fil"),
    ("Quraish", "Quraish"),
    ("Al-Maa'un", "Al-Maa'un"),
    ("Al-Kawthar", "Al-Kawthar"),
    ("Al-Kaafiroon", "Al-Kaafiroon"),
    ("An-Nasr", "An-Nasr"),
    ("Al-Masad", "Al-Masad"),
    ("Al-Ikhlaas", "Al-Ikhlaas"),
    ("Al-Falaq", "Al-Falaq"),
    ("An-Naas", "An-Naas"),
]


class Hafalan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hafalan")
    surat = models.CharField(max_length=75, choices=SURAHS)
    ayat_start = models.IntegerField(default=0)
    ayat_end = models.IntegerField(default=1)
    date = models.DateTimeField(blank=False, null=False, default=datetime.now())

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def total_ayat(self):
        return self.ayat_end - self.ayat_start + 1

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ------------> {self.surat} : {self.ayat_start} - {self.ayat_end}"


class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reset_token")
    token = models.CharField(default=secrets.token_hex(32), max_length=64, unique=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=False, null=False)
    expires_at = models.DateTimeField(default=datetime.now() + timedelta(minutes=30), blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_hex(32)
        if not self.expires_at:
            self.expires_at = datetime.now() + timedelta(minutes=30) # Token expires in 10 minutes

        super().save(*args, **kwargs)
