from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [


    path('ordercreate/', OrderAPICreate.as_view()),
    path('orderlist/', OrderAPIList.as_view()),
    path('orderdetail/', OrderAPIDetailView.as_view())


]
