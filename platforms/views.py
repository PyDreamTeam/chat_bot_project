import collections
from django.db.models import Q
from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.response import Response
from django.core.paginator import Paginator
from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag
from .serializers import (PlatformFilterSerializer, PlatformFilterSerializerSwagger, PlatformFilterSerializerSwaggerList, PlatformFilterSerializerSwaggerPost, PlatformFilterSerializerSwaggerPostResponses, PlatformFilterSerializerSwaggerPut, PlatformGroupSerializer, PlatformSearchResponseSerializer, PlatformSearchSerializer,
                          PlatformSerializer, PlatformSerializerSwagger, PlatformTagSerializer, PlatformFiltrationSerializerSwagger)
from accounts.permissions import get_permissions
from .utils import modify_data, get_groups_with_filters
from favorite.mixin_favorite import ManageFavoritePlatforms
from favorite.models import FavoritePlatforms
from drf_spectacular.utils import extend_schema
from django.contrib.contenttypes.models import ContentType
from accounts.services import add_platform_in_history
from accounts.tasks import add_platform_in_history_task


_TAG_PLATFORM = "Platform"
_TAG_PLATFORM_GROUP = "Platform group"
_TAG_PLATFORM_TAG = "Platform tag"
_TAG_PLATFORM_FAVORITE = "Platform favorite"
_TAG_PLATFORM_FILTRATION = "Platform filtration"
_TAG_PLATFORM_SEARCH = "Platform search"


@extend_schema(tags=[_TAG_PLATFORM_FAVORITE])
class PlatformFavoriteViewSet(viewsets.ModelViewSet, ManageFavoritePlatforms):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        user = request.user

        favorites = FavoritePlatforms.objects.filter(user=user)
        favorites_platform = []

        # Перебираем избранные объекты и добавляем связанные платформы в список
        for favorite in favorites:
            content_type = ContentType.objects.get_for_model(favorite.content_object)

            # Проверяем, является ли объект платформой
            if content_type.model == 'platform':
                favorites_platform.append(favorite.content_object)

        # Сериализуем список избранных платформ
        serializer = self.serializer_class(favorites_platform, many=True)
        return Response(serializer.data)


@extend_schema(tags=[_TAG_PLATFORM])
class PlatformViewSet(viewsets.ModelViewSet, ManageFavoritePlatforms):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    # вывод одного значения
    @extend_schema(
        responses={200: PlatformSerializerSwagger},
        )
    def retrieve(self, request, pk=None):
        is_favorite = False
        platform = self.queryset.filter(pk=pk).first()
        if platform:
            if request.user.is_authenticated:
                try:
                    add_platform_in_history_task.delay(user_id=request.user.id, platform_id=platform.id)
                except Exception as e:
                    print(e)
                    add_platform_in_history(user_id=request.user.id, platform_id=platform.id)
                favorite = FavoritePlatforms.objects.filter(user=request.user) & FavoritePlatforms.objects.filter(object_id=pk)
                if favorite:
                    is_favorite = True
            serializer = self.serializer_class(platform)

            platform_data = serializer.data
            data_platform = {
                "id": platform_data["id"],
                "title": platform_data["title"],
                "short_description": platform_data["short_description"],
                "full_description": platform_data["full_description"],
                "turnkey_solutions": platform_data["turnkey_solutions"],
                "price": platform_data["price"],
                "status": platform_data["status"],
                "created_at": platform_data["created_at"],
                "image": platform_data["image"],# if platform_data["image"] else "None",
                "link": platform_data["link"],
                "links_to_solution": platform_data["links_to_solution"],
                "is_favorite": is_favorite,
                "tags": [],

            }

            for platform_tag in platform.filter.all():
                tag_data = {
                    "id": platform_tag.id,
                    "tag": platform_tag.properties,
                    "image_tag": platform_tag.image, # if platform_tag.image else "None",
                    "status": platform_tag.status,
                    "is_message": platform_tag.is_message,
                }

                data_platform["tags"].append(tag_data)

            return Response(data_platform)
        else:
            return Response(
                {"message": "Platform not found."}, status=status.HTTP_404_NOT_FOUND
            )

    # вывод всех значений
    
    @extend_schema(
        responses={200: PlatformSerializerSwagger},
        )
    def list(self, request):
        platforms = Platform.objects.all()

        results = []

        # формирование списка групп
        for platform in platforms:
            serializer = self.serializer_class(platform)
            platform_data = serializer.data

            is_favorite = False
            if request.user.is_authenticated:
                favorite = FavoritePlatforms.objects.filter(user=request.user) & FavoritePlatforms.objects.filter(object_id=platform.id)
                if favorite:
                    is_favorite = True

            data_platform = {
                "id": platform_data["id"],
                "title": platform_data["title"],
                "short_description": platform_data["short_description"],
                "full_description": platform_data["full_description"],
                "turnkey_solutions": platform_data["turnkey_solutions"],
                "price": platform_data["price"],
                "status": platform_data["status"],
                "created_at": platform_data["created_at"],
                "image": platform_data["image"], #if platform_data["image"] else "None",
                "link": platform_data["link"],
                "links_to_solution": platform_data["links_to_solution"],
                "is_favorite": is_favorite,
                "tags": [],
            }

            for platform_tag in platform.filter.all():
                tag_data = {
                    "id": platform_tag.id,
                    "tag": platform_tag.properties,
                    "image_tag": platform_tag.image if platform_tag.image else "None",
                    "status": platform_tag.status,
                    "is_message": platform_tag.is_message,
                }

                data_platform["tags"].append(tag_data)

            results.append(data_platform)

        return Response(
            {"count": len(results), "next": None,
             "previous": None, "results": results}
        )


@extend_schema(tags=[_TAG_PLATFORM_GROUP])
class PlatformGroupViewSet(viewsets.ModelViewSet):
    queryset = PlatformGroup.objects.all()
    serializer_class = PlatformGroupSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


@extend_schema(tags=[_TAG_PLATFORM_FILTRATION])
class PlatformFilterViewSet(viewsets.ModelViewSet):
    queryset = PlatformFilter.objects.all()
    serializer_class = PlatformFilterSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.CoreJSONRenderer]
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


    # переопределил метод для  реализации создания тэгов при создании фильтров
    @extend_schema(
        request=PlatformFilterSerializerSwaggerPost,
        responses={200: PlatformFilterSerializerSwaggerPostResponses},
        description='Create a platform filter.',
        summary='Create platform filter',
        )
    def create(self, request):
        filter_data = request.data
        tags_data = filter_data.pop('tags')
        serializer = self.get_serializer(data=filter_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # создание и связывание тегов с созданным фильтром
        filter_instance = serializer.instance
        tags_data_with_title = []
        for tag_data in tags_data:
            tag_data['title'] = filter_instance.id
            tags_data_with_title.append(tag_data)
        tags_serializer = PlatformTagSerializer(data=tags_data_with_title, many=True)
        tags_serializer.is_valid(raise_exception=True)
        tags_serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   
    # обновление фильтров с тэгами
    @extend_schema(
        request=PlatformFilterSerializerSwaggerPut,
        responses={200: {'description': 'data updated'}},
        description='Update a platform filter.',
        summary='Update platform filter',
        )
    def update(self, request, patch_value=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        if not serializer.initial_data.get('group'):
            my_filter = PlatformFilter.objects.get(id=kwargs['pk'])
            test_filter = request.data
            test_filter['title'] = my_filter.title
            test_filter['group'] = my_filter.group.id
            serializer = self.get_serializer(instance, data=test_filter, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if not patch_value:
            self.update_tags(serializer)
        return Response("data updated", status=status.HTTP_200_OK)

    
    
    # patch запрос (перенаправляет на обновление put запроса)
    def partial_update(self, request, *args, **kwargs):
        patch_value = True
        return self.update(request, patch_value, *args, **kwargs)
    

    # обновление тэгов фильтра
    def update_tags(self, serializer):
        request_tags = set(tag_data.get('id') for tag_data in serializer.initial_data.get('tags'))
        filter_id = serializer.instance.id

        # Удаление тегов, которых нет в запросе и принадлежащих определенному фильтру
        PlatformTag.objects.filter(title_id=filter_id).exclude(id__in=request_tags).delete()

        for tag_data in serializer.initial_data.get('tags'):
            tag_id = tag_data.get('id')
            if tag_id:
                try:
                    tag = PlatformTag.objects.get(id=tag_id)
                    if tag_data.get('properties'):
                        tag.properties = tag_data.get('properties')
                    if tag_data.get('image_tag'):
                        tag.image = tag_data.get('image_tag')
                    if tag_data.get('status'):
                        tag.status = tag_data.get('status')
                    if tag_data.get('is_message'):    
                        tag.is_message = tag_data.get('is_message')
                    tag.save()
                except PlatformTag.DoesNotExist:
                    return Response("Tag does not exist", status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    filter_instance = serializer.instance
                    tag = PlatformTag.objects.create(
                        properties=tag_data.get('properties'),
                        image=tag_data.get('image_tag'),
                        status=tag_data.get('status'),
                        is_message=tag_data.get('is_message'),
                        title_id=filter_instance.id
                    )
                except Exception as e:
                    return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            
    # вывод одного значения
    @extend_schema(
        responses={200: PlatformFilterSerializerSwaggerList},
        description='A platform filter.',
        summary='A platform filter',
        )
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # код для включения тегов, принадлежащих данному фильтру
        filter_id = serializer.data['id']
        tags = PlatformTag.objects.filter(title_id=filter_id)
        tags_serializer = PlatformTagSerializer(tags, many=True)
        data = serializer.data
        list_for_OrderedDict = []
        for tag in tags_serializer.data:
            new_tag = dict(tag)
            new_tag['filter_id'] = new_tag['title']
            new_tag.pop('title')
            ordered_tag = collections.OrderedDict(new_tag)
            list_for_OrderedDict.append(ordered_tag)
        data['tags'] = list_for_OrderedDict
        return Response(data)


    # вывод всех значений
    @extend_schema(
        responses={200: PlatformFilterSerializerSwaggerList},
        description='List a platform filter.',
        summary='List a platform filter',
        )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        # код для включения тегов принадлежащих каждому фильтру
        serialized_data = serializer.data
        for data in serialized_data:
            filter_id = data['id']
            tags = PlatformTag.objects.filter(title_id=filter_id)
            tags_serializer = PlatformTagSerializer(tags, many=True)
            list_for_OrderedDict = []
            for tag in tags_serializer.data:
                new_tag = dict(tag)
                new_tag['filter_id'] = new_tag['title']
                new_tag.pop('title')
                tag = collections.OrderedDict(new_tag)
                list_for_OrderedDict.append(tag)
            data['tags'] = list_for_OrderedDict

        return Response(serialized_data)


@extend_schema(tags=[_TAG_PLATFORM_TAG])
class PlatformTagViewSet(viewsets.ModelViewSet):
    queryset = PlatformTag.objects.all()
    serializer_class = PlatformTagSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    # вывод всех значений
    def list(self, request):
        groups = PlatformGroup.objects.all()
        filters = PlatformFilter.objects.all()
        tags = PlatformTag.objects.all()

        results = []
        exceptions = ["Статистика", "Тарифы", "Техническая поддержка", "Уровень сложности", ]

        # формирование списка групп
        for group in groups:
            group_data = {
                "group": group.title,
                "id": group.id,
                "count": 0,
                "status": group.status,
                "filters": [],
            }

            # формирование списка фильтров по группам
            for platform_filter in filters.filter(group=group):
                filter_data = {
                    "filter": f"{platform_filter.title}"
                    if platform_filter.title not in exceptions
                    else "",
                    "id": platform_filter.id,
                    "image": "" if platform_filter.title in exceptions else platform_filter.image if platform_filter.image else "None",
                    "count": 0,
                    "status": platform_filter.status,
                    "functionality": platform_filter.functionality,
                    "integration": platform_filter.integration,
                    "multiple": platform_filter.multiple,
                    "tags": [],
                }

                # формирование списка тэгов по фильтрам
                for tag in tags.filter(title=platform_filter):
                    tag_data = {
                        "tag": tag.properties,
                        "id": tag.id,
                        "image_tag": tag.image if tag.image else "None",
                        "status": tag.status,
                        "is_message": tag.is_message,
                    }
                    filter_data["tags"].append(tag_data)
                    filter_data["count"] += 1

                group_data["filters"].append(filter_data)
                group_data["count"] += 1

            results.append(group_data)

        return Response(
            {"count": len(results), "next": None,
             "previous": None, "results": results}
        )


@extend_schema(tags=[_TAG_PLATFORM_FILTRATION],
               request=PlatformFiltrationSerializerSwagger,
               responses={
        200: PlatformSerializerSwagger(many=True),
    },)
class PlatformFiltration(generics.CreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Получаем параметры фильтра из запроса
        title = self.request.data.get("title")
        id_tags = self.request.data.get("id_tags", [])
        group = self.request.data.get("group")
        filter = self.request.data.get("filter")
        tag = self.request.data.get("tag")
        price_min = self.request.data.get("price_min")
        price_max = self.request.data.get("price_max")
        sort_abc = self.request.data.get("sort_abc")

        # Объект Q для хранения условий фильтрации
        q = Q()

        # Условие по title, если оно есть (поиск по имени)
        if title:
            q &= Q(title__icontains=title)

        # Условие по тегам, если они есть
        if id_tags:
            q &= Q(filter__id__in=id_tags)

        # Условие по имени группы, если оно есть
        if group:
            q &= Q(filter__title_id__group_id__title__icontains=group)

        # Условие по имени фильтра, если оно есть
        if filter:
            q &= Q(filter__title_id__title__icontains=filter)

        # Условие по имени тега, если оно есть
        if tag:
            q &= Q(filter__properties__icontains=tag)

        # Условие по минимальной цене, если она есть
        if price_min:
            q &= Q(price__gte=price_min)

        # Условие по максимальной цене, если она есть
        if price_max:
            q &= Q(price__lte=price_max)

        # Фильтрация
        if sort_abc == 'a':
            platforms = self.queryset.filter(q).order_by('title')
        elif sort_abc == 'z':
            platforms = self.queryset.filter(q).order_by('-title')
        else:
            platforms = self.queryset.filter(q)
        return platforms

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page_number = self.request.data.get("page_number") # номер страницы
        try:
            items_per_page = int(self.request.data.get("items_per_page", 10))
            if items_per_page == 0:
                items_per_page = 10
        except Exception:
            items_per_page = 10
        paginator = Paginator(queryset, items_per_page)
        page = paginator.get_page(page_number)

        if page is not None:
            serializer = self.serializer_class(page, many=True)
            modified_data = modify_data(serializer.data, len(queryset), page.number, paginator.num_pages)

            for platform_result in modified_data['results']:
                is_favorite = False
                platform = self.queryset.filter(pk=platform_result['id']).first()
                if platform:
                    if request.user.is_authenticated:
                        favorite = FavoritePlatforms.objects.filter(user=request.user) & FavoritePlatforms.objects.filter(object_id=platform_result['id'])
                        if favorite:
                            is_favorite = True
                platform_result['is_favorite'] = is_favorite
            return Response(modified_data)


@extend_schema(
    description='Endpoint for searching platforms',
    request=PlatformSearchSerializer,
    responses={
        200: PlatformSearchResponseSerializer(many=False),
    },
    tags=[_TAG_PLATFORM_SEARCH]
)
class PlatformSearch(generics.CreateAPIView):
    queryset_group = PlatformGroup.objects.all()
    queryset_filter = PlatformFilter.objects.all()
    serializer_class_group = PlatformGroupSerializer
    serializer_class_filter = PlatformFilterSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        title = self.request.data.get("title")
        # Используем Q-объект для выполнения поиска по полю title в обеих таблицах
        queryset_group = self.queryset_group.filter(title__icontains=title)
        queryset_filter = self.queryset_filter.filter(title__icontains=title)
        return queryset_group, queryset_filter
    
    def create(self, request, *args, **kwargs):
        queryset_group, queryset_filter = self.get_queryset()
        serialized_data_group = self.serializer_class_group(queryset_group, many=True).data
        serialized_data_filter = self.serializer_class_filter(queryset_filter, many=True).data

        response_data = {
            'count_group_results': len(serialized_data_group),
            'count_filter_results': len(serialized_data_filter),
            'search_results': {
                'group_results': get_groups_with_filters(queryset_group, PlatformFilter.objects.all()), 
                'filter_results': serialized_data_filter
            }
            }
        return Response(response_data)
