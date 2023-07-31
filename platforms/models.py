from django.db import models


class PlatformImage(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title},"


class PlatformGroup(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(PlatformImage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title},"


class PlatformFilter(models.Model):
    title = models.CharField(max_length=100)
    functionality = models.CharField(max_length=200, null=True)
    integration = models.CharField(max_length=800, null=True)
    multiple = models.BooleanField(default=True)
    group = models.ForeignKey(PlatformGroup, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    image = models.ForeignKey(PlatformImage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}, {self.group}"


class PlatformTag(models.Model):
    title = models.ForeignKey(PlatformFilter, on_delete=models.CASCADE)
    properties = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    image = models.ForeignKey(PlatformImage, on_delete=models.CASCADE, null=True)
    is_message = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.properties}"


class Platform(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=800)
    turnkey_solutions = models.IntegerField()
    filter = models.ManyToManyField(PlatformTag)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(PlatformImage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}, {self.short_description}"


