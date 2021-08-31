from django.db import models
from django.contrib.auth.models import AbstractUser   # what we use to create custom user


# Create your models here.
class CustomUser(AbstractUser):
    # null=True means a null entry can go to db
    # blank=True means no value is required in the form
    age = models.PositiveIntegerField(null=True, blank=True)
