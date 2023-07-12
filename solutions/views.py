from solutions.models import Solutions, Solution_filters, Filter_solutions
from rest_framework import viewsets
from solutions.serializer import SolutionSerializer, SolutionFilterSerializer, FilterSolutionSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(request=SolutionSerializer, tags=['Solutions'])
class SolutionsViewSet(viewsets.ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionSerializer


@extend_schema(request=SolutionFilterSerializer, tags=['SolutionFilter'])
class SolutionFilterViewSet(viewsets.ModelViewSet):
    queryset = Solution_filters.objects.all()
    serializer_class = SolutionFilterSerializer


@extend_schema(request=FilterSolutionSerializer, tags=['FilterSolutionr'])
class FilterSolutionViewSet(viewsets.ModelViewSet):
    queryset = Filter_solutions.objects.all()
    serializer_class = FilterSolutionSerializer
