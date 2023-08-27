from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import F, Subquery

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, generics, viewsets

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema

from .models import User, Profile, SolutionHistoryConfig, SolutionHistory
from .serializers import ProfileSerializer, UserCreatePasswordRetypeSerializer, \
    SolutionHistorySerializer


# Logout
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = TokenRefreshSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses={200: None})
    def post(self, request, *args, **kwargs):

        try:
            refresh_token = self.request.data.get('refresh')
            if not refresh_token:
                raise TokenError
            token = RefreshToken(token=refresh_token)
            token.blacklist()
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


# Profile
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        return profile


class SolutionHistoryViewSet(generics.ListAPIView):
    queryset = SolutionHistory.objects.all()
    serializer_class = SolutionHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        max_view_records = SolutionHistoryConfig.objects.get(pk=1).max_view_records
        queryset = SolutionHistory.objects.select_related("solution").annotate(
            time_difference=timezone.now() - F('action_time')
        ).filter(
            user=self.request.user,
            time_difference__lte=Subquery(
                SolutionHistoryConfig.objects.filter(pk=1)
                .values('record_expiry_hours')[:1]
            )
        ).order_by('-action_time').all()[:max_view_records]

        return queryset
