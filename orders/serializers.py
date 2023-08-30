from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('user', 'first_name', 'phone_number', 'comment', 'created_time', 'email')



