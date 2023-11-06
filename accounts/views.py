from datetime import timedelta

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

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from .models import User, Profile, SolutionHistoryConfig, SolutionHistory
from .permissions import IsAdminOrSuperAdmin
from .serializers import (
    ProfileSerializer,
    UserCreatePasswordRetypeSerializer,
    SolutionHistorySerializer,
    MaxViewRecordsSerializer,
    ExpiryPeriodSerializer,
)
from .services import get_solution_history


#Logout
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
    

#ListUser
class UserListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreatePasswordRetypeSerializer
    permission_classes = (IsAdminOrSuperAdmin,)
    
    
#Profile   
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        return profile


_TAG_SOLUTION_HISTORY = "Solution History"


class SolutionHistoryListView(generics.ListAPIView):
    queryset = SolutionHistory.objects.all()
    serializer_class = SolutionHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return get_solution_history(user=self.request.user)

    @extend_schema(tags=[_TAG_SOLUTION_HISTORY])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(self.get_serializer_data(serializer))

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.get_serializer_data(serializer))

    @staticmethod
    def get_serializer_data(serializer):
        serializer_data = [dct["solution"] for dct in serializer.data]
        for dct in serializer_data:
            dct["tags"] = dct.pop("filter")
        return serializer_data


class SolutionHistoryConfigBaseView(APIView):
    permission_classes = (IsAdminOrSuperAdmin,)
    serializer_class = None
    FIELD = ""

    def get(self, request, *args, **kwargs):
        queryset = SolutionHistoryConfig.objects.values(self.FIELD).get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        input_serializer = self.serializer_class(data=request.data)
        if input_serializer.is_valid(raise_exception=True):
            SolutionHistoryConfig.objects.filter(pk=1).update(
                **{self.FIELD: input_serializer.data.get(self.FIELD)}
            )
            return Response({"message": "Successfully changed"}, status=200)
        else:
            return Response(input_serializer.errors, status=400)


class MaxViewRecordsView(SolutionHistoryConfigBaseView):
    serializer_class = MaxViewRecordsSerializer
    FIELD = "max_view_records"

    @extend_schema(tags=[_TAG_SOLUTION_HISTORY])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=[_TAG_SOLUTION_HISTORY])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ExpiryPeriodView(SolutionHistoryConfigBaseView):
    serializer_class = ExpiryPeriodSerializer
    FIELD = "expiry_period"

    @extend_schema(tags=[_TAG_SOLUTION_HISTORY])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=[_TAG_SOLUTION_HISTORY],
        parameters=[
            OpenApiParameter(
                name=FIELD,
                description="Store timedelta objects. Format: [DD] [[HH:]MM:]ss[.uuuuuu]",
                required=True,
                type=timedelta,
                examples=[
                    OpenApiExample("1 day 8 hours 55 min 30 seconds", value="1 8:55:30"),
                    OpenApiExample("30 days", value="30 00:00:00"),
                    OpenApiExample("12 hours", value="12:00:00"),
                    OpenApiExample("45 min", value="45:00"),
                    OpenApiExample("20 seconds", value="20"),
                ],
            )
        ],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
