from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet



from . import views as views_accounts

router = DefaultRouter()
router.register("user", views_accounts.UserViewSet)

urlpatterns = [
    path('userlist/', views_accounts.UserApiView.as_view()),
    path('userlist/<int:pk>/', views_accounts.UserApiView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # djoser
    re_path(r'^user/reset_password_confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', UserViewSet.as_view({'post': 'reset_password_confirm'}, name='password_reset_confirm'))
] + router.urls

