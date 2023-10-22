from rest_framework import serializers

from .models import Solution, SolutionFilter, SolutionGroup, SolutionTag, Cards, Advantages, Dignities, Steps


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
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


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = "__all__"


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = "__all__"


class DignitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dignities
        fields = "__all__"


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = "__all__"