from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"bots", BotsViewSet)
router.register(r"business-area", BusinessAreaViewSet)
router.register(r"business-target", BusinessTargetViewSet)
router.register(r"functional", FunctionalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
