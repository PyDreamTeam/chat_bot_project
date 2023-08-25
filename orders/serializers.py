from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(write_only=True)
    comment = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = ['first_name', 'email', 'phone_number', 'comment']


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None

        if user:
            order = Order.objects.create(user=user,
                                         phone_number=validated_data['phone_number'],
                                         comment=validated_data['comment'])
        else:
            order = Order.objects.create(phone_number=validated_data['phone_number'],
                                         comment=validated_data['comment'])

        return order