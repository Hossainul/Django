# Generated by Django 5.2 on 2025-07-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_profile_car_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
