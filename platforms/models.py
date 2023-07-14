from django.db import models


class PlatformFilter(models.Model):
    title = models.CharField(max_length=100)
    functionality = models.CharField(max_length=200)
    integration = models.CharField(max_length=500, null=True, blank=True)
    properties = models.JSONField()
    image = models.ImageField(null=True, upload_to='./platforms/platformfilter_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}, {self.properties}'


class Platform(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to='./platforms/platform_images/')
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=800)
    turnkey_solutions = models.IntegerField()
    filter = models.ManyToManyField(PlatformFilter)
    price = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}, {self.short_description}'
