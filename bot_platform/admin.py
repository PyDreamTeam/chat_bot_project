from django.contrib import admin
from .models import BusinessArea, BusinessTarget, Functional, Bots



@admin.register(BusinessArea)
class BusinessAreaAdmin(admin.ModelBusinessArea):
    list_display = ('name')


@admin.register(BusinessTarget)
class BusinessTargetAdmin(admin.ModelBusinessTarget):
    list_display = ('name')


@admin.register(Functional)
class FunctionalAdmin(admin.ModelFunctional):
    list_display = ('name')


@admin.register(Bots)
class BotsAdmin(admin.ModelBots):
    list_display = ('title', 'description', 'image', 'business_area', 'business_target', 'fuctional', 'type_platform')   


