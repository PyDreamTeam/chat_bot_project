from django.urls import path
from .views import OrdersViewSet


urlpatterns = [
    path('ordercreate/', OrdersViewSet.as_view({'post':'create'})),
    path('orderlist/', OrdersViewSet.as_view({'get':'list'})),
    path('orderlist/<int:pk>/', OrdersViewSet.as_view({'get':'retrieve'})),
    path('orderdetail/<int:pk>/', OrdersViewSet.as_view({'put':'update', 'delete':'destroy'})),
]
