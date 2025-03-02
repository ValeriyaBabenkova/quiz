from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class Profile(models.Model):
    name_team = models.OneToOneField(User, on_delete=models.CASCADE)


# Create your models here.
