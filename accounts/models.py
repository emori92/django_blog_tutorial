from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """Model definition for CustomUser."""

    class Meta:
        verbose_name_plural = 'CustomUsers'

    def __str__(self):
        return self.username