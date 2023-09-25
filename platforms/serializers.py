from rest_framework import serializers

from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag


class PlatformSerializer(serializers.ModelSerializer):
    # is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        model = Platform
        fields = "__all__"
        print(fields)

    # def get_is_favorite(self, obj):
    #     # Здесь вы должны определить, является ли объект избранным для текущего пользователя
    #     # Ваша логика определения статуса is_favorite здесь
    #     # Например, вы можете проверить, есть ли соответствующая запись в модели Favorite
    #     user = self.context['request'].user
    #     print(user)
    #     favorite = Favorite.objects.filter(user=user, content_type=ContentType.objects.get_for_model(obj), object_id=obj.id).exists()
    #     return favorite


class PlatformTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformTag
        fields = "__all__"


class PlatformGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformGroup
        fields = "__all__"


class PlatformFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFilter
        fields = "__all__"
