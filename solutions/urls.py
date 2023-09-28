from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SolutionFilterViewSet, SolutionFiltration,
                    SolutionGroupViewSet, SolutionTagViewSet,
                    SolutionViewSet)

router = DefaultRouter()
router.register("solutions", SolutionViewSet)
router.register("groups", SolutionGroupViewSet)
router.register("filters", SolutionFilterViewSet)
router.register("tags", SolutionTagViewSet)

urlpatterns = [
    path(
        "solution/filtration/", SolutionFiltration.as_view(), name="solution-filtration"
    ),
    path("solution/", include(router.urls)),
]