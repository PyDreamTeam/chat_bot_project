from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone

"""
OrdersViewSet processes applications from registered and unregistered users
and save them in the database
"""

class OrdersViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """
        registered users are processed here and their data is stored in the database.
        """
        if self.request.user.is_authenticated:

            serializer.save(user=self.request.user, created_time=timezone.now())
            """
            unregistered users are processed here and their data is stored in the database.
            """
        else:
            serializer.save(created_time=timezone.now())

