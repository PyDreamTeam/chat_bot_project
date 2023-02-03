from django.urls import path, include
from django.contrib.auth import views
from .views import UserRegistration


urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='registration'), #User Registration
    path('login/', views.LoginView.as_view(), name='login'), #User login
    path('logout/', views.LogoutView.as_view(), name='logout'), #User logout
]