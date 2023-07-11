from django.contrib import admin
from platforms.models import Platform, PlatformFilter

@admin.register(Platform)
class Platform1Admin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(PlatformFilter)
class PlatformFilter1Admin(admin.ModelAdmin):
    list_display = ("title", )
