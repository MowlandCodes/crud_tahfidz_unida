# Generated by Django 5.1.4 on 2025-01-07 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0036_alter_hafalan_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresettoken',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 22, 44, 36, 5779)),
        ),
        migrations.AlterField(
            model_name='passwordresettoken',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 23, 14, 36, 5793)),
        ),
        migrations.AlterField(
            model_name='passwordresettoken',
            name='token',
            field=models.CharField(default='3534946e8501efcaf578657e8d54e1dc39b48f2f259a7ca8a698397189521bf5', max_length=64, unique=True),
        ),
    ]
