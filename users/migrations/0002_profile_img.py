# Generated by Django 4.2.10 on 2024-02-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="Img",
            field=models.ImageField(
                default="profiles_images/default.jpg",
                upload_to="profiles_images/{instance.username.username}/{filename}",
                verbose_name="Image",
            ),
        ),
    ]