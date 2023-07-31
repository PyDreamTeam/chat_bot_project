from django.db import transaction
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, generics, viewsets

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import TokenError

from djoser import views, utils
from djoser.conf import settings
from djoser.compat import get_user_email

from drf_spectacular.utils import extend_schema

from .models import User, Profile
from .serializers import ProfileSerializer, UserCreatePasswordRetypeSerializer


# Logout
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = TokenRefreshSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses={200: None})
    def post(self, request, *args, **kwargs):
        # all devices
        # if self.request.data.get('all'):

        #     token = OutstandingToken
        #     for token in OutstandingToken.objects.filter(user=request.user):
        #         _, _ = BlacklistedToken.objects.get_or_create(token=token)
        #     return Response(status=status.HTTP_200_OK)

        # token blacklist
        try:
            refresh_token = self.request.data.get('refresh')
            if not refresh_token:
                raise TokenError
            token = RefreshToken(token=refresh_token)
            token.blacklist()
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    # def get_object(self):
    #     return self.request.user.profile
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     user = self.request.user
    #     profile = self.get_object()
    #
    #     profile.delete()
    #     user.delete()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)
