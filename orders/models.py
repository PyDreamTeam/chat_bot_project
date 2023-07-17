from django.db import models


class Order(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
