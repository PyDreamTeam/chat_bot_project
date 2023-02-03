from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from api.serializers import UserSerializer


class UserRegistration(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():

            return Response(serializer.data, status=status.HTTP_201_CREATED)  
            # new_user = User.objects.create(
            #     email=request.data['email'],
            #     first_name=request.data['first_name'],
            #     last_name =request.data['last_name'],
            #     user_role=request.data['user_role'],            
            #     password=request.data['password']
            # )  
            # return Response(new_user, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        