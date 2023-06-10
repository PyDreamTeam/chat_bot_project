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
    email = models.EmailField(_('email'), unique=True, blank=False)
    user_role = models.CharField(choices=Role.choices, default="User")
    get_email_notifications = models.BooleanField(blank=False, default=False)
    #wish = models.ManyToManyField(Wish, _('wish'), blank=False)
    #photo = models.ImageField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email  
