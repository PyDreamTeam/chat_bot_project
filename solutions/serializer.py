from rest_framework import serializers
from solutions.models import Solutions, Solution_filters, Filter_solutions


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solutions
        fields = "__all__"
    
    

class SolutionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution_filters
        fields = '__all__'


class FilterSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_solutions
        fields = '__all__'    

    