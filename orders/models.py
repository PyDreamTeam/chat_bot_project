from django.db import models
from accounts.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13)
    comment = models.CharField(max_length=200)


