from rest_framework import serializers

from .models import Platform, PlatformFilter, PlatformGroup, PlatformImage, PlatformTag


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class PlatformTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformTag
        fields = "__all__"


class PlatformGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformGroup
        fields = "__all__"


class PlatformFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFilter
        fields = "__all__"


class PlatformImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformImage
        fields = "__all__"
