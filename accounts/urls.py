from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LogoutAPIView, ProfileDetailView, SolutionHistoryListView, MaxViewRecordsView, \
    ExpiryPeriodView

urlpatterns = [
    
    # base urls:
    path('auth/', include('djoser.urls')),
    # JWT-endpoints:
    path('auth/', include('djoser.urls.jwt')),
    # JWT Logout
    path('auth/logout/', LogoutAPIView.as_view(), name="api-logout"),
    # Profile url
    path('profile/', ProfileDetailView.as_view(), name='user-profile-detail'),

    path('history/solutions/', SolutionHistoryListView.as_view(), name='history-solutions'),

    path('history/solutions/max-view-records', MaxViewRecordsView.as_view(),
         name='history-solutions-max-view-records'),

    path('history/solutions/expiry-period', ExpiryPeriodView.as_view(),
         name='history-solutions-expiry-period'),
]
