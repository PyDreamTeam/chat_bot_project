from rest_framework import serializers

from .models import Solution, SolutionFilter, SolutionGroup, SolutionTag, Cards, Advantages, Dignities, Steps


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = "__all__"


class SolutionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionTag
        fields = "__all__"


class SolutionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionGroup
        fields = "__all__"


class SolutionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionFilter
        fields = "__all__"


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = "__all__"


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = "__all__"


class DignitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dignities
        fields = "__all__"


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = "__all__"


# request swagger для фильтрации
class SolutionSerializerSwaggerFiltrationRequest(serializers.Serializer):
    title = serializers.CharField(required=False)
    id_tags = serializers.ListField(child=serializers.IntegerField(), required=False)
    # group = serializers.CharField(required=False)
    # filter = serializers.CharField(required=False)
    # tag = serializers.CharField(required=False)
    price_min = serializers.FloatField(required=False)
    price_max = serializers.FloatField(required=False)
    sort_abc = serializers.ChoiceField(choices=[('a', 'a'), ('z', 'z')], required=False)
    page_number = serializers.IntegerField(required=False)
    items_per_page = serializers.IntegerField(required=False, default=10)


# response swagger для фильтрации
class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tag = serializers.CharField()
    image_tag = serializers.CharField()
    is_active = serializers.BooleanField()
    is_message = serializers.BooleanField()

class SolutionSerializerSwaggerFiltrationResponse(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    business_model = serializers.CharField()
    business_area = serializers.CharField()
    business_niche = serializers.CharField()
    objective = serializers.CharField()
    solution_type = serializers.CharField()
    short_description = serializers.CharField()
    platform = serializers.CharField()
    messengers = serializers.CharField()
    integration_with_CRM = serializers.CharField()
    integration_with_payment_systems = serializers.CharField()
    tasks = serializers.CharField()
    actions_to_complete_tasks = serializers.CharField()
    image = serializers.CharField()
    price = serializers.IntegerField()
    filter = serializers.ListField(child=serializers.IntegerField())
    is_active = serializers.BooleanField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    turnkey_platform = serializers.CharField()
    link = serializers.CharField()
    links_to_platform = serializers.CharField()
    tags = TagSerializer(many=True)


# response swagger для списка тэгов
class TagSerializerSwaggerListResponse(serializers.Serializer):
    tag = serializers.CharField()
    id = serializers.IntegerField()
    image_tag = serializers.CharField()
    status = serializers.CharField()
    is_message = serializers.BooleanField()

class FilterSerializerSwaggerListResponse(serializers.Serializer):
    filter = serializers.CharField()
    id = serializers.IntegerField()
    image = serializers.CharField()
    count = serializers.IntegerField()
    status = serializers.CharField()
    functionality = serializers.CharField()
    integration = serializers.CharField()
    multiple = serializers.BooleanField()
    tags = TagSerializerSwaggerListResponse(many=True)

class ResponseSerializerSwaggerListResponse(serializers.Serializer):
    group = serializers.CharField()
    id = serializers.IntegerField()
    count = serializers.IntegerField()
    status = serializers.CharField()
    filters = FilterSerializerSwaggerListResponse(many=True)