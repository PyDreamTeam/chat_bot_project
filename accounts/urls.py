from django.urls import path, include
from django.contrib.auth import views
from . import views as views_accounts


urlpatterns = [
    path('registration/', views_accounts.UserRegistration.as_view(), name='registration'), #User Registration
    path('login/', views.LoginView.as_view(), name='login'), #User login
    path('logout/', views.LogoutView.as_view(), name='logout'), #User logout
    path('userlist/', views_accounts.UserApiView.as_view()),
    path('userlist/<int:pk>/', views_accounts.UserApiView.as_view()),
]