from django.db import models
from accounts.models import User





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=42, null=True)
    phone_number = models.CharField(max_length=13)
    comment = models.CharField(max_length=200)
    created_time = models.DateTimeField(blank=True,  null=True)
    email = models.EmailField()





