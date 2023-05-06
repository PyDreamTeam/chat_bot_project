from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views as views_accounts
from .views import CustomTokenCreateView, CustomTokenDestroyView


router = DefaultRouter()
router.register("user", views_accounts.UserViewSet)

urlpatterns = [
    path('userlist/', views_accounts.UserApiView.as_view()),
    path('userlist/<int:pk>/', views_accounts.UserApiView.as_view()),
    path('change-password/', views_accounts.ChangePasswordView.as_view(), name='change-password'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # djoser
    path('auth/token/create/', CustomTokenCreateView.as_view(), name='token_create'),
    path('auth/token/destroy/', CustomTokenDestroyView.as_view(), name='token_destroy'),
    #re_path(r'^user/reset_password_confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views_accounts.UserViewSet.as_view({'post': 'reset_password_confirm'}, name='password_reset_confirm'))
] + router.urls
