from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views as views_accounts


urlpatterns = [
    path('user/', views_accounts.UserViewSet.as_view({'post': 'create'}, name='user-registration')),
    path('change-password/', views_accounts.ChangePasswordView.as_view(), name='change-password'),
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),  # djoser
    path('auth/token/create/', views_accounts.CustomTokenCreateView.as_view(), name='token_create'),
    path('auth/token/destroy/', views_accounts.CustomTokenDestroyView.as_view(), name='token_destroy'),
    re_path(r'^user/reset_password_confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views_accounts.UserViewSet.as_view({'post': 'reset_password_confirm'}, name='password_reset_confirm')),
    path("user/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]# + router.urls