from django.db import models


class BusinessArea(models.Model):
    name = models.CharField(max_length=50, blank=True)


class BusinessTarget(models.Model):
    name = models.CharField(max_length=50, blank=True)


class Functional(models.Model):
    name = models.CharField(max_length=50, blank=True)



class Bots(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500, help_text="Enter information about bot", blank=True)
    image = models.ImageField(null=True, blank=False)
    business_area = models.ManyToManyField(BusinessArea, blank=True)
    business_target = models.ManyToManyField(BusinessTarget, blank=True)
    fuctional = models.ManyToManyField(Functional, blank=True)
    type_platform = models.CharField(max_length=50, blank=True)




    
