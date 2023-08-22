from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class OrderAPICreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            existing_data = {
                'first_name': user.first_name,
                'email': user.email,
            }
            data = {**existing_data, **request.data}
        else:
            data = request.data

        serializer = OrderSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            application = serializer.save()
            return Response({'message': "Successfully created", 'id': application.id}, status=201)
        else:
            return Response(serializer.errors, status=400)


class OrderAPIList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
