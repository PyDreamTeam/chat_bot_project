from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


# OrdersViewSet processes applications from registered and unregistered users and save them in the database
class OrdersViewSet(viewsets.GenericViewSet,
                    viewsets.mixins.CreateModelMixin,
                    viewsets.mixins.RetrieveModelMixin,
                    viewsets.mixins.UpdateModelMixin,
                    viewsets.mixins.DestroyModelMixin,
                    viewsets.mixins.ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    # этот метод для получения заявок по токену (пока не работает, как нужно)
    def get_queryset(self):

        if self.request.user.is_authenticated:

            return Order.objects.filter(user=self.request.user)

        else:
            return Order.objects.all()

    def perform_create(self, serializer):

        # registered users are processed here and their data is stored in the database.
        if self.request.user.is_authenticated:

            serializer.save(user=self.request.user, created_time=timezone.now())

        # unregistered users are processed here and their data is stored in the database.
        else:
            serializer.save(created_time=timezone.now())
