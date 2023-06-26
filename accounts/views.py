from django.db import transaction
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, generics


# from rest_framework_simplejwt.tokens import (
#     OutstandingToken,
#     BlacklistedToken,
#     RefreshToken
# )
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from djoser import views, utils
from djoser.conf import settings
from djoser.compat import get_user_email

from .models import User
from .serializers import UserCreateSerializer


#Logout
class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token = OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response(status=status.HTTP_200_OK)
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_200_OK)