from rest_framework import viewsets
from .serializers import *


class BotsViewSet(viewsets.ModelViewSet):
    queryset = Bots.objects.all()
    serializer_class = BotsSerializer


class BusinessAreaViewSet(viewsets.ModelViewSet):
    queryset = BusinessArea.objects.all()
    serializer_class = BusinessAreaSerializer


class BusinessTargetViewSet(viewsets.ModelViewSet):
    queryset = BusinessTarget.objects.all()
    serializer_class = BusinessTargetSerializer


class FunctionalViewSet(viewsets.ModelViewSet):
    queryset = Functional.objects.all()
    serializer_class = FunctionalSerializer


from django.shortcuts import render

# Create your views here.
