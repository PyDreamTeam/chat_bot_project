from django.db import transaction
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, \
    UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User as UserModel
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ["email", "first_name", "last_name", "user_role", "password"]

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = UserModel

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
