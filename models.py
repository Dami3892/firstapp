
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomerUser(AbstractUser):
    phone_number = models.charField(max_length=12, blank=True)
