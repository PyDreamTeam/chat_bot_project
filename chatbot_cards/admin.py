from django.contrib import admin
from .models import BusinessArea, BusinessTarget, Functional, Bots


@admin.register(BusinessArea)
class BusinessAreaAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(BusinessTarget)
class BusinessTargetAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Functional)
class FunctionalAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Bots)
class BotsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
        "display_business_area",
        "display_business_target",
        "display_fuctional",
        "type_platform",
    )
