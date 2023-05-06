from django.db import transaction
from djoser.conf import settings
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserCreateSerializer, ChangePasswordSerializer
from djoser import views
from djoser.views import TokenCreateView

from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _
from djoser.views import TokenDestroyView
from django.contrib.auth import authenticate


class UserViewSet(views.UserViewSet):

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(email=request.data.get('email'))
        headers = self.get_success_headers(serializer.data)
        token, _ = settings.TOKEN_MODEL.objects.get_or_create(user=user)
        token_serializer_class = settings.SERIALIZERS.token
        response = {
            "id": str(user.id),
            "email": serializer.data.get('email'),
            "first_name": serializer.data.get('first_name'),
            "last_name": serializer.data.get('last_name'),
            "user_role": serializer.data.get('user_role'),
            "emailNotification": serializer.data.get('emailNotification'),
            "auth_token": token_serializer_class(token).data.get('token'),
        }
        if serializer.data.get('avatar'):
            response['avatar'] = serializer.data.get('avatar')
        return Response(data=response, status=status.HTTP_201_CREATED, headers=headers)

class CustomTokenCreateView(TokenCreateView):

    def _action(self, serializer):
        user = serializer.instance
        token = utils.login_user(self.request, user)
        data = {
            'id': str(user.id),
            'email': serializer.data.get('email'),
            'first_name': serializer.data.get('first_name'),
            'last_name': serializer.data.get('last_name'),
            'user_role': serializer.data.get('user_role'),
            'emailNotification': serializer.data.get('emailNotification'),
            'auth_token': token
        }
        return Response(data=data, status=status.HTTP_200_OK)


class CustomTokenDestroyView(TokenDestroyView):
    def post(self, request, *args, **kwargs):
        utils.logout_user(request)
        serializer = self.get_serializer(data=request.data)
        data = {
            'id': str(user.id),
            'email': serializer.data.get('email'),
            'first_name': serializer.data.get('first_name'),
            'last_name': serializer.data.get('last_name'),
            'user_role': serializer.data.get('user_role'),
            'emailNotification': serializer.data.get('emailNotification'),
            'auth_token': None
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class UserApiView(APIView):

    def get(self, request):
        user_data = User.objects.all()
        return Response({'users': UserCreateSerializer(user_data, many=True).data})


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": [_("Wrong password.")]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'message': _('Password updated successfully'),
            }

            return Response(response, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
