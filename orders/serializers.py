from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.tasks import send_message_when_new_order_task
from .models import Order

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'first_name', 'phone_number', 'comment', 'created_time', 'email', 'id')

    # correct filling of all fields in the database
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None

        if user:
            order = Order.objects.create(user=user,
                                         first_name=user.first_name,
                                         phone_number=validated_data['phone_number'],
                                         comment=validated_data['comment'],
                                         created_time=validated_data['created_time'],
                                         email=user.email)
        else:
            order = Order.objects.create(first_name=validated_data['first_name'],
                                         phone_number=validated_data['phone_number'],
                                         comment=validated_data['comment'],
                                         created_time=validated_data['created_time'],
                                         email=validated_data['email'])
        if order.id:
            send_message_when_new_order_task.delay(order.id)
        return order
