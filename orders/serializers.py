from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Order
        fields = ['first_name', 'email', 'phone_number', 'comment']
