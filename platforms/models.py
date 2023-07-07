from django.db import models


class PlatformFilter(models.Model):
    title = models.CharField(max_length=255)
    properties = models.JSONField()

    def __str__(self):
        return f'{self.title}, {self.properties}'


class Platform(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    full_description = models.CharField(max_length=255)
    turnkey_solutions = models.IntegerField()
    filter = models.ManyToManyField(PlatformFilter)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.short_description}'
