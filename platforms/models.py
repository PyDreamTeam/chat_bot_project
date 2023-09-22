from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.postgres.fields import ArrayField
from favorite.models import Favorite



class PlatformGroup(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=800, default='save')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title},"


class PlatformFilter(models.Model):
    title = models.CharField(max_length=100)
    functionality = models.CharField(max_length=200, null=True)
    integration = models.CharField(max_length=800, null=True)
    multiple = models.BooleanField(default=True)
    group = models.ForeignKey(PlatformGroup, on_delete=models.CASCADE)
    status = models.CharField(max_length=800, default='save')
    image = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}, {self.group}"


class PlatformTag(models.Model):
    title = models.ForeignKey(PlatformFilter, on_delete=models.CASCADE)
    properties = models.CharField(max_length=1000)
    status = models.CharField(max_length=800, default='save')
    image = models.TextField(null=True, blank=True)
    is_message = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.properties}"


class Platform(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200, null=True)
    full_description = models.CharField(max_length=800, null=True)
    turnkey_solutions = models.IntegerField(null=True)
    filter = models.ManyToManyField(PlatformTag, null=True)
    price = models.IntegerField(null=True)
    status = models.CharField(max_length=800, default='save', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=800, null=True)
    links_to_solution = ArrayField(models.CharField(max_length=10000), null=True, blank=True)
    # create new field to correct work app favorite
    favorites = GenericRelation(Favorite)

    def __str__(self):
        return f"{self.title}, {self.short_description}"
