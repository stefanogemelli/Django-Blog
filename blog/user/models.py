from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()

class User(AbstractUser):
    full_name = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField(upload_to="Profiles",blank=True, null=True)
    profession = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    birthdate = models.DateTimeField(null=True)
    twitter = models.URLField(max_length=50, null=True)
    linkedin = models.URLField(max_length=50, null=True)
    facebook = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    if created:
        print("Envío de email al registrarse, la config actual está obsoleta por cambios en la api de google")

        # send_mail(
        # "Subject here",
        # "Here is the message. Welcome, you have successfully on our site",
        # os.getenv("EMAIL_HOST_USER"),
        # [instance.email],
        # )   



