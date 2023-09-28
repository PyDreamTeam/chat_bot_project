from rest_framework import serializers

from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag


class PlatformSerializer(serializers.ModelSerializer):
    # is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        model = Platform
        fields = "__all__"
        print(fields)


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
