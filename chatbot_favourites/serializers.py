__author__ = 'ValPirate'

from rest_framework import serializers
from .models import Bot_favourites

class Bot_favourites_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bot_favourites
        fields = '__all__'

