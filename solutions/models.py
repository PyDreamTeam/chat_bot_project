from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from favorite.models import FavoriteSolutions
from django.contrib.postgres.fields import ArrayField
from django.forms import JSONField


class SolutionGroup(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=800, null=True)
    status = models.CharField(max_length=50, default="save")

    def __str__(self):
        return f"{self.title},"


class SolutionFilter(models.Model):
    title = models.CharField(max_length=100)
    functionality = models.CharField(max_length=200, null=True)
    integration = models.CharField(max_length=800, null=True)
    multiple = models.BooleanField(default=True)
    group = models.ForeignKey(SolutionGroup, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=800, null=True)
    status = models.CharField(max_length=50, default="save")

    def __str__(self):
        return f"{self.title}, {self.group}"


class SolutionTag(models.Model):
    title = models.ForeignKey(SolutionFilter, on_delete=models.CASCADE)
    properties = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=800, null=True)
    is_message = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="save")

    def __str__(self):
        return f"{self.title}, {self.properties}"


class Cards(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    img = models.CharField(max_length=200)


class Advantages(models.Model):
    advantage = models.CharField(max_length=200)


class Dignities(models.Model):
    dignities = models.CharField(max_length=200)


class Steps(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    media = models.TextField(null=True, blank=True)


class Solution(models.Model):
    title = models.CharField(max_length=100)
    business_model = models.CharField(max_length=200)
    business_area = models.CharField(max_length=100)
    business_niche = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    solution_type = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    platform = models.CharField(max_length=100)
    messengers = models.CharField(max_length=100)
    status = models.CharField(max_length=800, default='save', null=True, blank=True)
    integration_with_CRM = models.CharField(max_length=100)
    integration_with_payment_systems = models.CharField(max_length=100)
    tasks = models.CharField(max_length=100)
    actions_to_complete_tasks = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField(null=True)
    filter = models.ManyToManyField(SolutionTag)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    advantages = models.ManyToManyField(Advantages)
    subtitle = models.CharField(max_length=300)
    full_description = models.CharField(max_length=300)
    dignities = models.ManyToManyField(Dignities)
    steps = models.ManyToManyField(Steps)
    cards = models.ManyToManyField(Cards)
    cards_title = models.CharField(max_length=200)
    cards_description = models.CharField(max_length=200)
    steps_title = models.CharField(max_length=200)
    steps_description = models.CharField(max_length=200)
    turnkey_platform = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=800, null=True, blank=True)
    links_to_platform = ArrayField(models.CharField(max_length=10000), null=True, blank=True)
    dignities = ArrayField(models.CharField(max_length=10000), null=True, blank=True)
    # create new field to correct work app favorite
    favorites = GenericRelation(FavoriteSolutions)
    # subtitle = models.CharField(max_length=300)
    # full_description = models.CharField(max_length=300)
    

    def __str__(self):
        return f"{self.title}, {self.short_description}, {self.id}"


class Tariff(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_special = models.CharField(max_length=100, null=True, blank=True)
    tags_of_rates = models.JSONField()
    
    def __str__(self):
        return f"{self.id}, {self.title}, {self.price}"
