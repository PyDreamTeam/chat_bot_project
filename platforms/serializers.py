from rest_framework import serializers
from .models import Platform, PlatformFilter

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class PlatformFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFilter
        fields = '__all__'