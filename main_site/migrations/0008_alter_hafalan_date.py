# Generated by Django 5.1.4 on 2024-12-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_remove_hafalan_ayat_hafalan_ayat_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hafalan',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
