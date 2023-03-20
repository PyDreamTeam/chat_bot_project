__author__ = 'ValPirate'

from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'favourites', Bot_favourites')),

urlpatterns = [
    path('', include(router.urls)),
]