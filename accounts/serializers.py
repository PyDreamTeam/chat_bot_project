from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from djoser.conf import settings

from djoser.serializers import UserCreatePasswordRetypeSerializer as BaseUserCreatePasswordRetypeSerializer, UserCreateSerializer
from djoser.serializers import SendEmailResetSerializer

from rest_framework import serializers
from .models import Profile, SolutionHistoryConfig, PlatformHistoryConfig

from solutions.serializers import SolutionSerializer, SolutionTagSerializer
from platforms.serializers import PlatformSerializer, PlatformTagSerializer
from .models import Profile, SolutionHistory, PlatformHistory

User = get_user_model()


#User Create    
class UserCreatePasswordRetypeSerializer(BaseUserCreatePasswordRetypeSerializer):

    class Meta(BaseUserCreatePasswordRetypeSerializer.Meta):
        model = User
        fields = (
                    "email",
                    "first_name",
                    "last_name",
                    "user_role",
                    "password",
                    "get_email_notifications",
                    "is_active"
                )

    # Active users def
    # def perform_create(self, validated_data):
    #     with transaction.atomic():
    #         user = User.objects.create_user(**validated_data)
    #         if settings.SEND_ACTIVATION_EMAIL:
    #             user.is_active = True
    #             user.save(update_fields=["is_active"])
    #     return user


#User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                    'id',
                    "email",
                    "first_name",
                    "last_name",
                    "user_role",
                    "get_email_notifications",
                    "is_active"
                )
    

#Password
class PasswordResetSerializer(SendEmailResetSerializer):
    
    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise ValidationError('Email not found')

        return value


#Profile
class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    user_role = serializers.CharField(source='user.user_role')
    email = serializers.CharField(source='user.email', read_only=True)
    phone_number = serializers.CharField(allow_null=True)
    image = serializers.CharField(allow_null=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'user_role', 'email', 'phone_number', 'image']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.image = validated_data.get('image', instance.image)

        instance.user.save()
        instance.save()
        return instance


#Solution History
class SolutionSerializerInAccounts(SolutionSerializer):
    filter = SolutionTagSerializer(many=True)


class SolutionHistorySerializer(serializers.ModelSerializer):
    solution = SolutionSerializerInAccounts()

    class Meta:
        model = SolutionHistory
        fields = ("solution", )


class SolutionMaxViewRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionHistoryConfig
        fields = ("max_view_records", )


class SolutionExpiryPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionHistoryConfig
        fields = ("expiry_period", )


#Platform History
class PlatformSerializerInAccounts(PlatformSerializer):
    filter = PlatformTagSerializer(many=True)


class PlatformHistorySerializer(serializers.ModelSerializer):
    platform = PlatformSerializerInAccounts()

    class Meta:
        model = PlatformHistory
        fields = ("platform", )
        
        
class PlatformMaxViewRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformHistoryConfig
        fields = ("max_view_records", )


class PlatformExpiryPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformHistoryConfig
        fields = ("expiry_period", )