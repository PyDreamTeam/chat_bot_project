from django.db import models
from accounts.models import User


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    comment = models.CharField(max_length=200)


