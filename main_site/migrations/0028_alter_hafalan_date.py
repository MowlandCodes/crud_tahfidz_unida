# Generated by Django 5.1.4 on 2025-01-04 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0027_alter_hafalan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hafalan',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 4, 20, 32, 47, 436545)),
        ),
    ]
