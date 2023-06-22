from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import APILogoutView


urlpatterns = [
    
    # base urls:
    path('auth/', include('djoser.urls')),
    # JWT-endpoints:
    path('auth/', include('djoser.urls.jwt')),
    # JWT Logout
    path('auth/logout/', APILogoutView.as_view(), name="api-logout"),
   
]