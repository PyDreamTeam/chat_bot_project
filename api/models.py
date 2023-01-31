from django.db import models


class User(models.Model):
    name = models.CharField(max_length=55, null=False)
    surname = models.CharField(max_length=55)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=55, null=False)
