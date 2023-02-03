import djoser as djoser
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/drf-auth/', include("rest_framework.urls")),  # default Django authorization
    path('api/v1/auth/', include('djoser.urls')),  # djoser
    path('api/v1/auth/', include('djoser.urls.authtoken')),  # djoser
    path('api/v1/accounts/', include('accounts.urls')), #include api accounts
    path('api/v1/userlist/', views.UserApiView.as_view()),
    path('api/v1/userlist/<int:pk>/', views.UserApiView.as_view()),
]

