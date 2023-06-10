from django.db import transaction
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from rest_framework.decorators import action
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
