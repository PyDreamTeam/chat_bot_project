from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from djoser.conf import settings
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import SendEmailResetSerializer

from rest_framework import serializers


User = get_user_model()


class UserCreateSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = (
                    "email",
                    "first_name",
                    "last_name",
                    "user_role",
                    "password",
                    "get_email_notifications"
                )

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


class PasswordResetSerializer(SendEmailResetSerializer):
    
    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise ValidationError('Email not found')
        return value