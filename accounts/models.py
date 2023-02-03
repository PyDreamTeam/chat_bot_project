from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    USER_ROLE = [
        ('USER', "User"),
        ('ADMIN', "Admin"),
        ('MANAGER', "Manager"),
    ]

    username = None
    email = models.EmailField(_('email'), unique=True)
    user_role = models.CharField(max_length=10, choices=USER_ROLE, default='User')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    def __str__(self):
        return self.email  
