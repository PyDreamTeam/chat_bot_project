from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from config import settings
from solutions.models import Solution
from platforms.models import Platform
from .managers import CustomUserManager


class Role(models.TextChoices):
    user = "US", _("User")
    superadmin = "SA", _("SuperAdmin")
    admin = "AD", _("Admin")
    manager = "MN", _("Manager")


ALL_ROLES = (Role.superadmin, Role.user, Role.admin, Role.manager)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email'), db_index=True, unique=True, blank=False)
    user_role = models.CharField(max_length=10, choices=Role.choices, default="US")
    get_email_notifications = models.BooleanField(blank=False, default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_role', 'get_email_notifications', 'is_active']
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    image = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.email


#Solution History
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

    def __str__(self):
        return f"user: {self.user}, solution: {self.solution}"


class SolutionHistoryConfig(models.Model):
    max_view_records = models.IntegerField()
    expiry_period = models.DurationField()

    def __str__(self):
        return f"max_view_records: {self.max_view_records}, " \
               f"expiry_period: {self.expiry_period}"


#Platform History
class PlatformHistory(models.Model):
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
    platform = models.ForeignKey(
        Platform,
        on_delete=models.CASCADE,
        verbose_name=_("platform"),
    )

    def __str__(self):
        return f"user: {self.user}, platform: {self.platform}"
    
    
class PlatformHistoryConfig(models.Model):
    max_view_records = models.IntegerField()
    expiry_period = models.DurationField()

    def __str__(self):
        return f"max_view_records: {self.max_view_records}, " \
               f"expiry_period: {self.expiry_period}"