from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from config import settings
from solutions.models import Solution
from .managers import CustomUserManager


class Role(models.TextChoices):
    user = "US", _("User")
    superadmin = "SA", _("SuperAdmin")
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
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.email


class SolutionHistory(models.Model):
    action_time = models.DateTimeField(
        verbose_name=_("action time"),
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
    )
    solution = models.ForeignKey(
        Solution,
        on_delete=models.CASCADE,
        verbose_name=_("solution"),
    )


class SolutionHistoryConfig(models.Model):
    max_view_records = models.IntegerField()
    record_expiry_hours = models.DurationField()
