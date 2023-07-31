from django.contrib import admin

from accounts.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_role", "get_email_notifications", )