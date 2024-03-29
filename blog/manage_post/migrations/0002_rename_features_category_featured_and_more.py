# Generated by Django 5.0.3 on 2024-03-12 00:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_post", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="features",
            new_name="featured",
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(upload_to="Articles"),
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(upload_to="Categories"),
        ),
    ]
