from django.urls import path
from .views import OrdersViewSet


urlpatterns = [
    path('ordercreate/', OrdersViewSet.as_view({'post':'create'})),
    path('orderlist/', OrdersViewSet.as_view({'get':'list'})),
    path('orderdetail/<int:pk>/', OrdersViewSet.as_view({'put':'update'})),
]
