# Generated by Django 5.0.3 on 2024-03-14 06:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_alter_profile_photo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="birthdate",
            new_name="birthday",
        ),
    ]
