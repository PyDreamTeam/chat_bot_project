import djoser as djoser
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/drf-auth/', include("rest_framework.urls")),  # default Django authorization
    path('api/v1/auth/', include('djoser.urls')),  # djoser
    path('api/v1/auth/', include('djoser.urls.authtoken')),  # djoser
    path('api/v1/accounts/', include('accounts.urls')), #include api accounts
]
