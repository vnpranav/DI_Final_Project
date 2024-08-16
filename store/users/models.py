from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here if needed
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username