__author__ = 'ValPirate'

from rest_framework import serializers
from .models import Bots, BusinessArea, BusinessTarget, Functional

class BotsSerializer(serializers.ModelSerializer):
    business_area = serializers.StringRelatedField(many=True)
    business_target = serializers.StringRelatedField(many=True)
    fuctional = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bots
        fields = ['id', 'title', 'description', 'image', 'business_area', 'business_target', 'fuctional', 'type_platform']

class BusinessAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessArea
        fields = '__all__'


class BusinessTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTarget
        fields = '__all__'


class FunctionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functional
        fields = '__all__'