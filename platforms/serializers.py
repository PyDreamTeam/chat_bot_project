from rest_framework import serializers

from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag


class PlatformSerializer(serializers.ModelSerializer):
    # is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        model = Platform
        fields = "__all__"


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


# для документации swagger
class PlatformSearchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)


class PlatformSearchResponseSerializer(serializers.Serializer):
    count_group_results = serializers.IntegerField()
    count_filter_results = serializers.IntegerField()
    search_results = serializers.ListField(child=(serializers.DictField()))


class PlatformTagSerializerSwagger(serializers.Serializer):
    id = serializers.CharField()
    properties = serializers.CharField()
    status = serializers.CharField()
    image = serializers.CharField()
    is_message = serializers.CharField()
    title = serializers.CharField()

class PlatformFilterSerializerSwagger(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    status = serializers.CharField()
    group = serializers.IntegerField()
    functionality = serializers.CharField()
    integration = serializers.CharField()
    multiple = serializers.BooleanField
    tags = PlatformTagSerializerSwagger(many=True)

class PlatformTagSerializerSwaggerPost(serializers.Serializer):
    properties = serializers.CharField()
    status = serializers.CharField(required=False)
    image = serializers.CharField(required=False)
    is_message = serializers.BooleanField(required=False)


class PlatformFilterSerializerSwaggerPost(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    status = serializers.CharField()
    group = serializers.IntegerField()
    functionality = serializers.CharField()
    integration = serializers.CharField()
    multiple = serializers.BooleanField()
    tags = PlatformTagSerializerSwaggerPost(many=True)

class PlatformFilterSerializerSwaggerPostResponses(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    status = serializers.CharField()
    group = serializers.IntegerField()
    functionality = serializers.CharField()
    integration = serializers.CharField()
    multiple = serializers.BooleanField()


class PlatformTagSerializerSwaggerList(serializers.Serializer):
    id = serializers.IntegerField()
    properties = serializers.CharField()
    status = serializers.CharField()
    image = serializers.CharField()
    is_message = serializers.BooleanField()
    filter_id = serializers.CharField()


class PlatformFilterSerializerSwaggerList(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.CharField()
    status = serializers.CharField()
    group = serializers.IntegerField()
    functionality = serializers.CharField()
    integration = serializers.CharField()
    multiple = serializers.BooleanField()
    tags = PlatformTagSerializerSwaggerList(many=True)


class PlatformFilterSerializerSwaggerPut(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    status = serializers.CharField()
    group = serializers.IntegerField()
    functionality = serializers.CharField()
    integration = serializers.CharField()
    multiple = serializers.BooleanField()
    tags = PlatformTagSerializerSwaggerList(many=True)