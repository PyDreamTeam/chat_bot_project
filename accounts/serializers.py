from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "user_role", "password"]
        # read_only_fields = ['password']

# class UserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=55)
#     email = serializers.EmailField(max_length=254)
#     password = serializers.CharField(min_length=8, max_length=55)

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.email = validated_data.get("email", instance.email)
#         instance.password = validated_data.get("password", instance.password)
#         instance.save()
#         return instance
