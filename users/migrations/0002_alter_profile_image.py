# Generated by Django 4.2.4 on 2023-10-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.jpeg", upload_to="profile_pics"),
        ),
    ]
