from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Role(models.TextChoices):
    user = "US", _("User")
    admin = "AD", _("Admin")
    manager = "MN", _("Manager")


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email'), db_index=True, unique=True, blank=False)
    user_role = models.CharField(max_length=10, choices=Role.choices, default="US")
    get_email_notifications = models.BooleanField(blank=False, default=False)
    #wish = models.ManyToManyField(Wish, _('wish'), blank=False)
    #photo = models.ImageField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_role', 'get_email_notifications']
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.email
