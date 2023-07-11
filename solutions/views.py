
from solutions.models import Solutions
from rest_framework import viewsets
from solutions.serializer import SolutionSerializer


class SolutionsViewSet(viewsets.ModelViewSet):
    queryset = Solutions.all()
    serializer_class = SolutionSerializer



