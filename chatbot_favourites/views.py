from rest_framework import viewsets
from .serializers import *


class Bot_favouritesViewSet(viewsets.ModelViewSet):
    queryset = Bot_favourites.objects.all()
    serializer_class = Bot_favourites_serializer