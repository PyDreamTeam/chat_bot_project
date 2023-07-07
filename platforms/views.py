from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Platform, PlatformFilter
from .serializers import PlatformSerializer, PlatformFilterSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformFilterViewSet(viewsets.ModelViewSet):
    queryset = PlatformFilter.objects.all()
    serializer_class = PlatformFilterSerializer