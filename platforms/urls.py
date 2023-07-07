from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatformViewSet, PlatformFilterViewSet

router = DefaultRouter()
router.register('platforms', PlatformViewSet)
router.register('platform-filters', PlatformFilterViewSet)

urlpatterns = [
    path('platforms/', include(router.urls)),
]