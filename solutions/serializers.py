from rest_framework import serializers

from .models import Solution, SolutionFilter, SolutionGroup, SolutionTag, FavoriteSolutions


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution, FavoriteSolutions
        fields = "__all__"


class SolutionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionTag
        fields = "__all__"


class SolutionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionGroup
        fields = "__all__"


class SolutionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionFilter
        fields = "__all__"