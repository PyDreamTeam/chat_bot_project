from django.contrib import admin
from .models import User


@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "user_role", "password", "get_email_notifications"]
