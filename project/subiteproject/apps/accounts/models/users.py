"""User model"""

# Base User model
from django.contrib.auth.models import AbstractUser

# Models
from django.db import models

# Date and time
from django.utils import timezone

# Regex
from django.core.validators import RegexValidator


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField('Email', null=False, blank=False, unique=True)
    user_created_at = models.DateTimeField(default=timezone.now)
    user_updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_created_at = timezone.now()
        self.user_updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)