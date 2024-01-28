from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (LogoutAPIView, ProfileDetailView,
                    SolutionHistoryListView, SolutionMaxViewRecordsView, 
                    SolutionExpiryPeriodView, PlatformHistoryListView, PlatformMaxViewRecordsView,
                    PlatformExpiryPeriodView, UsersAPIView, UserSearchView)


router = DefaultRouter()
router.register("users", UsersAPIView)


urlpatterns = [   
     # base urls:
     path('auth/', include('djoser.urls')),
     # JWT-endpoints:
     path('auth/', include('djoser.urls.jwt')),
     # JWT Logout
     path('auth/logout/', LogoutAPIView.as_view(), name="api-logout"),
     # Profile url
     path('profile/', ProfileDetailView.as_view(), name='user-profile-detail'),
     # Users url
     path("account/", include(router.urls)),
     # Users-search url
     path('users/search/', UserSearchView.as_view(), name='user-search'),
     # User history Solution url:
     path('history/solutions/', SolutionHistoryListView.as_view(), name='history-solutions'),
     path('history/solutions/max-view-records', SolutionMaxViewRecordsView.as_view(),
          name='history-solutions-max-view-records'),
     path('history/solutions/expiry-period', SolutionExpiryPeriodView.as_view(),
          name='history-solutions-expiry-period'),
     # User history Platform url:
     path('history/platforms/', PlatformHistoryListView.as_view(), name='history-platforms'),
     path('history/platforms/max-view-records', PlatformMaxViewRecordsView.as_view(),
          name='history-platforms-max-view-records'),
     path('history/platforms/expiry-period', PlatformExpiryPeriodView.as_view(),
          name='history-platforms-expiry-period'),
]
