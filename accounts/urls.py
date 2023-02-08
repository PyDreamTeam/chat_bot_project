from django.urls import path, include

from . import views as views_accounts


urlpatterns = [
    # path('signup/',  views.UserViewSet.as_view(), name='signup'), #User Registration
    path('userlist/', views_accounts.UserApiView.as_view()),
    path('userlist/<int:pk>/', views_accounts.UserApiView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # djoser
]
