# Generated by Django 5.1.4 on 2025-01-04 16:13

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0029_alter_hafalan_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='hafalan',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 4, 23, 13, 9, 348120)),
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reset_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
