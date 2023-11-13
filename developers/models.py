from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


# class Worker(AbstractUser):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField(unique=True)

class Developer(AbstractBaseUser):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [first_name,last_name,email]