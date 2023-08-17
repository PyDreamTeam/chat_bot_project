from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (PlatformFilterViewSet, PlatformFiltration,
                    PlatformGroupViewSet, PlatformTagViewSet,
                    PlatformViewSet)

router = DefaultRouter()
router.register("platforms", PlatformViewSet)
router.register("groups", PlatformGroupViewSet)
router.register("filters", PlatformFilterViewSet)
router.register("tags", PlatformTagViewSet)

urlpatterns = [
    path(
        "platform/filtration/", PlatformFiltration.as_view(), name="platform-filtration"
    ),
    # path("platform/search/", PlatformSearch.as_view(), name="platform-search"),
    path("platform/", include(router.urls)),
]
