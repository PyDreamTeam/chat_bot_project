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

from .models import User


#Logout
class APILogoutView(generics.GenericAPIView):
    serializer_class = TokenRefreshSerializer
    permission_classes = (IsAuthenticated,)    

    def post(self, request, *args, **kwargs):
        #all devices
        # if self.request.data.get('all'):
        #     token = OutstandingToken
        #     for token in OutstandingToken.objects.filter(user=request.user):
        #         _, _ = BlacklistedToken.objects.get_or_create(token=token)
        #     return Response(status=status.HTTP_200_OK)
        
        #token blacklist        
        try:
            refresh_token = self.request.data.get('refresh')
            if not refresh_token:
                raise TokenError
            token = RefreshToken(token=refresh_token)
            token.blacklist() 
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)            
        
        return Response(status=status.HTTP_200_OK)