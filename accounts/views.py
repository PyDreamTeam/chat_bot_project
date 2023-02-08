from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserCreateSerializer

# class UserRegistration(APIView):
#
#     def post(self, request):
#         serializer = UserCreateSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         User.objects.create_user(
#             serializer.data.get('email'),
#             serializer.data.get('password')
#         )
#         return Response(status=status.HTTP_201_CREATED)


class UserApiView(APIView):

    def get(self, request):
        user_data = User.objects.all()
        return Response({'users': UserCreateSerializer(user_data, many=True).data})
