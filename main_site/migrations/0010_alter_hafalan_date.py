# Generated by Django 5.1.4 on 2025-01-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0009_alter_hafalan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hafalan',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
