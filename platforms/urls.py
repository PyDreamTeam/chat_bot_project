from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (PlatformFilterViewSet, PlatformFiltration,
                    PlatformGroupViewSet, PlatformTagViewSet,
                    PlatformViewSet, PlatformFavoriteViewSet, PlatformSearch)


router = DefaultRouter()
router.register("platforms", PlatformViewSet)
router.register("platforms-favorite", PlatformFavoriteViewSet)
router.register("groups", PlatformGroupViewSet)
router.register("filters", PlatformFilterViewSet)
router.register("tags", PlatformTagViewSet)


urlpatterns = [
    path("platform/filtration/", PlatformFiltration.as_view(), name="platform-filtration"),
    path("platform/filters-search/", PlatformSearch.as_view(), name="platform-search"),
    path("platform/", include(router.urls)),
]
