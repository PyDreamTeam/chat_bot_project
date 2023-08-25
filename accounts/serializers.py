from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from djoser.conf import settings

from djoser.serializers import UserCreatePasswordRetypeSerializer as BaseUserCreatePasswordRetypeSerializer
from djoser.serializers import SendEmailResetSerializer

from rest_framework import serializers
from .models import Profile


User = get_user_model()

    
class UserCreatePasswordRetypeSerializer(BaseUserCreatePasswordRetypeSerializer):

    class Meta(BaseUserCreatePasswordRetypeSerializer.Meta):
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
                user.is_active = True
                user.save(update_fields=["is_active"])
        return user
    
    
class PasswordResetSerializer(SendEmailResetSerializer):
    
    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise ValidationError('Email not found')

        return value


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_number = serializers.CharField()
    image = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'image']


