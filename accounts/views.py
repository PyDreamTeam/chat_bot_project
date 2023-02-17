from django.db import transaction
from djoser.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserCreateSerializer
from djoser import views


class UserViewSet(views.UserViewSet):

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer = self.get_serializer(data=request.data, get_email_notifications=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(email=request.data.get('email'))
        headers = self.get_success_headers(serializer.data)
        token, _ = settings.TOKEN_MODEL.objects.get_or_create(user=user)
        token_serializer_class = settings.SERIALIZERS.token
        return Response(
            data=token_serializer_class(token).data,
            status=status.HTTP_201_CREATED, headers=headers)


class UserApiView(APIView):

    def get(self, request):
        user_data = User.objects.all()
        return Response({'users': UserCreateSerializer(user_data, many=True).data})
