from django.urls import path, include, re_path
from rest_framework_simplejwt import views
from . import views as views_accounts
from .views import LogoutUserView
from djoser import views as djoser_views


urlpatterns = [
    path('user/registration', views_accounts.UserViewSet.as_view({'post': 'create'}, name='user-registration')),
    path("user/login", views.TokenObtainPairView.as_view(), name="login"),
    path('user/change-password/', views_accounts.ChangePasswordView.as_view(), name='change-password'),
    path('user/reset_password', djoser_views.UserViewSet.as_view({'post': 'reset password'}, name='reset-password')),
    path('user/logout/', LogoutUserView.as_view(), name='user-logout'),

    re_path(r"^user/jwt/refresh/?", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^user/jwt/verify/?", views.TokenVerifyView.as_view(), name="jwt-verify"),
    re_path(r'^user/reset_password_confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views_accounts.UserViewSet.as_view({'post': 'reset_password_confirm'}, name='password_reset_confirm'))

]

#from rest_framework.routers import DefaultRouter
#outer = DefaultRouter()
#router.register("user", views_accounts.UserViewSet)
# path('userlist/', views_accounts.UserApiView.as_view()),
# path('userlist/<int:pk>/', views_accounts.UserApiView.as_view()),

# + router.urls

