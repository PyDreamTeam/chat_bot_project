from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as views_accounts

router = DefaultRouter()
router.register("user", views_accounts.UserViewSet)

urlpatterns = [
    path('userlist/', views_accounts.UserApiView.as_view()),
    path('userlist/<int:pk>/', views_accounts.UserApiView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # djoser
] + router.urls

