from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField()
    comment = serializers.CharField()

    class Meta:
        model = Order
        fields = ['first_name', 'email', 'phone_number', 'comment']

    def create(self, validated_data):
        user_data = validated_data.pop('user', {})
        user_first_name = user_data.get('first_name')
        user_email = user_data.get('email')

        user = User.objects.create(first_name=user_first_name, email=user_email)

        order = Order.objects.create(user=user,
                                     phone_number=validated_data['phone_number'],
                                     comment=validated_data['comment'])
        return order
