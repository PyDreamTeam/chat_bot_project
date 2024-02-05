from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SolutionFilterViewSet, SolutionFiltration,
                    SolutionGroupViewSet, SolutionTagViewSet,
                    SolutionViewSet, CardsViewSet, AdvantagesViewSet, DignitiesViewSet, StepsViewSet, SolutionSearch, TariffViewSet)


router = DefaultRouter()
router.register("solutions", SolutionViewSet)
router.register("groups", SolutionGroupViewSet)
router.register("filters", SolutionFilterViewSet)
router.register("tags", SolutionTagViewSet)
# router.register("cards", CardsViewSet)
# router.register("advantages", AdvantagesViewSet)
# router.register("dignities", DignitiesViewSet)
# router.register("steps", StepsViewSet)
router.register("tariffs", TariffViewSet)   


urlpatterns = [
    path("solution/filtration/", SolutionFiltration.as_view(), name="solution-filtration"),
    path("solution/filters-search/", SolutionSearch.as_view(), name="platform-search"),
    path("solution/", include(router.urls)),
]