from django.contrib import admin

from orders.models import Order


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone", "text",)


from django.contrib import admin

# Register your models here.
