from django.contrib import admin

from platforms.models import (Platform, PlatformFilter, PlatformGroup,
                              PlatformTag)


@admin.register(Platform)
class Platform1Admin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(PlatformTag)
class PlatformTag1Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "properties",
    )


@admin.register(PlatformFilter)
class PlatformTag1Admin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(PlatformGroup)
class PlatformTag1Admin(admin.ModelAdmin):
    list_display = ("title",)
