from datetime import timedelta

from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import F, Subquery

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, generics, viewsets, mixins

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from .models import User, Profile, SolutionHistoryConfig, SolutionHistory, PlatformHistoryConfig, PlatformHistory
from .permissions import IsAdminOrSuperAdmin
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    UserCreateSerializer,
    UserCreatePasswordRetypeSerializer,
    SolutionHistorySerializer,
    SolutionMaxViewRecordsSerializer,
    SolutionExpiryPeriodSerializer,
    PlatformHistorySerializer,
    PlatformMaxViewRecordsSerializer,
    PlatformExpiryPeriodSerializer,
)
from .services import get_solution_history, get_platform_history


_TAG_SOLUTION_HISTORY = "Solution History"
_TAG_PLATFORM_HISTORY = "Platform History"
_TAG_USERS = "Users"
_TAG_USER_SEARCH = "Users search"
_TAG_PROFILE = "Profile"


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
    

#Users
@extend_schema(tags=[_TAG_USERS])
class UsersAPIView(mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSuperAdmin,)     


#Users searching
@extend_schema(
    description='Endpoint for searching users',
    tags=[_TAG_USER_SEARCH]
)
class UserSearchView(generics.ListAPIView):     
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSuperAdmin,)
    
    def get_queryset(self):   
        queryset = User.objects.all()       
        first_name = self.request.data.get('first_name', None)
        last_name = self.request.data.get('last_name', None)
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
            
        return queryset      
    
    
#Profile   
@extend_schema(tags=[_TAG_PROFILE])
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        return profile


#Solution History
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


class SolutionMaxViewRecordsView(SolutionHistoryConfigBaseView):
    serializer_class = SolutionMaxViewRecordsSerializer
    FIELD = "max_view_records"

    @extend_schema(tags=[_TAG_SOLUTION_HISTORY])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=[_TAG_SOLUTION_HISTORY])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SolutionExpiryPeriodView(SolutionHistoryConfigBaseView):
    serializer_class = SolutionExpiryPeriodSerializer
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
    

#Platform History
class PlatformHistoryListView(generics.ListAPIView):
    queryset = PlatformHistory.objects.all()
    serializer_class = PlatformHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return get_platform_history(user=self.request.user)

    @extend_schema(tags=[_TAG_PLATFORM_HISTORY])
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
        serializer_data = [dct["platform"] for dct in serializer.data]
        for dct in serializer_data:
            dct["tags"] = dct.pop("filter")
        return serializer_data
    
    
class PlatformHistoryConfigBaseView(APIView):
    permission_classes = (IsAdminOrSuperAdmin,)
    serializer_class = None
    FIELD = ""

    def get(self, request, *args, **kwargs):
        queryset = PlatformHistoryConfig.objects.values(self.FIELD).get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        input_serializer = self.serializer_class(data=request.data)
        if input_serializer.is_valid(raise_exception=True):
            PlatformHistoryConfig.objects.filter(pk=1).update(
                **{self.FIELD: input_serializer.data.get(self.FIELD)}
            )
            return Response({"message": "Successfully changed"}, status=200)
        else:
            return Response(input_serializer.errors, status=400)
        
        
class PlatformMaxViewRecordsView(PlatformHistoryConfigBaseView):
    serializer_class = PlatformMaxViewRecordsSerializer
    FIELD = "max_view_records"

    @extend_schema(tags=[_TAG_PLATFORM_HISTORY])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=[_TAG_PLATFORM_HISTORY])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    
class PlatformExpiryPeriodView(PlatformHistoryConfigBaseView):
    serializer_class = PlatformExpiryPeriodSerializer
    FIELD = "expiry_period"

    @extend_schema(tags=[_TAG_PLATFORM_HISTORY])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=[_TAG_PLATFORM_HISTORY],
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