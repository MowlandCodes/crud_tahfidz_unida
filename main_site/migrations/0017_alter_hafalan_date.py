# Generated by Django 5.1.4 on 2025-01-04 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0016_alter_hafalan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hafalan',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 4, 16, 15, 53, 515633)),
        ),
    ]
