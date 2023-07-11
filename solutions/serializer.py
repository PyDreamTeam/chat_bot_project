from rest_framework import serializers
from solutions.models import Solutions


class SolutionSerializer(serializers.Serializer):
    class Meta:
        model = Solutions
        fields = "__all__"
    
    

    

    