from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LogoutAPIView, ProfileDetailView


urlpatterns = [
    
    # base urls:
    path('auth/', include('djoser.urls')),
    # JWT-endpoints:
    path('auth/', include('djoser.urls.jwt')),
    # JWT Logout
    path('auth/logout/', LogoutAPIView.as_view(), name="api-logout"),
    # profile
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='user-profile-detail'),   
]