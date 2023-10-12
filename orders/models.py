from django.db import models
from config import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=42, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    comment = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField(blank=True,  null=True)
    email = models.EmailField()





