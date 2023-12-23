from django.db.models.signals import post_save
from django.dispatch import receiver
from config import settings
from .models import User, Profile
from django.db.models.signals import post_migrate
from django.db import IntegrityError


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    try:
        email = settings.SUPERUSER_EMAIL
        password = settings.SUPERUSER_PASSWORD
        if not User.objects.filter(email=email).exists():
            admin = User.objects.create_superuser(email, password)
            print('Superuser "admin" created successfully')
    except IntegrityError:
        print('Superuser "admin" already exists')
