from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (PlatformFilterViewSet, PlatformGroupViewSet,
                    PlatformTagViewSet, PlatformViewSet)

router = DefaultRouter()
router.register("platforms", PlatformViewSet)
router.register("groups", PlatformGroupViewSet)
router.register("filters", PlatformTagViewSet)
router.register("tags", PlatformFilterViewSet)

urlpatterns = [
    path("platform/", include(router.urls)),
]
