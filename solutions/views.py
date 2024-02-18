import collections
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.response import Response
from accounts.services import add_solution_in_history

from accounts.tasks import add_solution_in_history_task
from .models import Solution, SolutionFilter, SolutionGroup, SolutionTag, Cards, Advantages, Dignities, Steps, Tariff
from .serializers import (FilterSerializerSwaggerListRequest, FilterSerializerSwaggerListResponse, SolutionFilterSearchSerializer, SolutionFilterSearchSerializerResponse, SolutionFilterSerializer, SolutionGroupSerializer, 
                          SolutionSerializer, SolutionTagSerializer, SolutionTagSerializer, CardsSerializer, AdvantagesSerializer, DignitiesSerializer, StepsSerializer, SolutionSerializerSwaggerFiltrationRequest, SolutionSerializerSwaggerFiltrationResponse, ResponseSerializerSwaggerListResponse, TariffSerializer)
from accounts.permissions import get_permissions
from .utils import get_groups_with_filters, modify_data
from drf_spectacular.utils import extend_schema
from favorite.mixin_favorite import ManageFavoriteSolutions
from favorite.models import FavoriteSolutions


_TAG_SOLUTION = "Solution"
_TAG_SOLUTION_GROUP = "Solution group"
_TAG_SOLUTION_TAG = "Solution tag"
_TAG_SOLUTION_FAVORITE = "Solution favorite"
_TAG_SOLUTION_FILTRATION = "Solution filtration"
_TAG_SOLUTION_SEARCH = "Solution search"
_TAG_SOLUTION_FILTERS_SEARCH = "Solution filters search"


@extend_schema(tags=[_TAG_SOLUTION])
class SolutionViewSet(viewsets.ModelViewSet, ManageFavoriteSolutions):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    # вывод одного значения
    def retrieve(self, request, pk=None):
        solution = self.queryset.filter(pk=pk).first()
        is_favorite = False
        if solution:
            if request.user.is_authenticated:
                try:
                    add_solution_in_history_task.delay(user_id=request.user.id, solution_id=solution.id)
                except Exception as e:
                    print(e)
                    add_solution_in_history(user_id=request.user.id, solution_id=solution.id)
                favorite_solutions = FavoriteSolutions.objects.filter(user=request.user) & FavoriteSolutions.objects.filter(object_id=pk)
                if favorite_solutions:
                    is_favorite = True
            serializer = self.serializer_class(solution)
            solution_data = serializer.data
            data_solution = {
                "id": solution_data["id"],
                "title": solution_data["title"],
                "short_description": solution_data["short_description"],
                "status": solution_data["status"],
                "advantages": solution_data["advantages"],
                "full_description": solution_data["full_description"],
                "steps": solution_data["steps"],
                "image": solution_data["image"],
                "price": solution_data["price"],
                "filter": solution_data["filter"],
                "created_at": solution_data["created_at"],
                "dignities": solution_data["dignities"],
                "cards": solution_data["cards"],
                "steps_title": solution_data["steps_title"],
                "steps_description": solution_data["steps_description"],
                "link": solution_data["link"],
                "links_to_platform": solution_data["links_to_platform"],
                "dignities": solution_data["dignities"],
                "is_favorite": is_favorite, #app favorite
                "tags": [],
            }

            for solution_tag in solution.filter.all():
                tag_data = {
                    "id": solution_tag.id,
                    "tag": solution_tag.properties,
                    "image_tag": solution_tag.image if solution_tag.image else "None",
                    "is_active": solution_tag.is_active,
                    "is_message": solution_tag.is_message,
                }

                data_solution["tags"].append(tag_data)
            return Response(data_solution)
        else:
            return Response(
                {"message": "Solution not found."}, status=status.HTTP_404_NOT_FOUND
            )

    # вывод всех значений

    def list(self, request):
        solutions = Solution.objects.all()

        results = []

        # формирование списка групп
        for solution in solutions:
            serializer = self.serializer_class(solution)
            solution_data = serializer.data

            is_favorite = False
            if request.user.is_authenticated:
                favorite_solutions = FavoriteSolutions.objects.filter(user=request.user) & FavoriteSolutions.objects.filter(object_id=solution.id)
                if favorite_solutions:
                    is_favorite = True

            data_solution = {
                "id": solution_data["id"],
                "title": solution_data["title"],
                # "business_model": solution_data["business_model"],
                # "business_area": solution_data["business_area"],
                # "business_niche": solution_data["business_niche"],
                # "objective": solution_data["objective"],
                # "solution_type": solution_data["solution_type"],
                "short_description": solution_data["short_description"],
                # "platform": solution_data["platform"],
                # "platform_title": solution_data["platform_title"],
                # "platform_image": solution_data["platform_image"],
                # "messengers": solution_data["messengers"],
                "status": solution_data["status"],
                # "integration_with_CRM": solution_data["integration_with_CRM"],
                # "integration_with_payment_systems": solution_data["integration_with_payment_systems"],
                # "actions_to_complete_tasks": solution_data["actions_to_complete_tasks"],
                "advantages": solution_data["advantages"],
                # "subtitle": solution_data["subtitle"],
                "full_description": solution_data["full_description"],
                "steps": solution_data["steps"],
                "image": solution_data["image"],
                "price": solution_data["price"],
                "filter": solution_data["filter"],
                # "is_active": solution_data["is_active"],
                "created_at": solution_data["created_at"],
                "dignities": solution_data["dignities"],
                "cards": solution_data["cards"],
                # "cards_title": solution_data["cards_title"],
                # "cards_description": solution_data["cards_description"],
                "steps_title": solution_data["steps_title"],
                "steps_description": solution_data["steps_description"],
                # "turnkey_platform": solution_data["turnkey_platform"],
                "link": solution_data["link"],
                "links_to_platform": solution_data["links_to_platform"],
                "dignities": solution_data["dignities"],
                "is_favorite": is_favorite, #app favorite
                "tags": [],
            }

            for solution_tag in solution.filter.all():
                tag_data = {
                    "id": solution_tag.id,
                    "tag": solution_tag.properties,
                    "image_tag": solution_tag.image if solution_tag.image else "None",
                    "is_active": solution_tag.is_active,
                    "is_message": solution_tag.is_message,
                }

                data_solution["tags"].append(tag_data)

            results.append(data_solution)

        return Response(
            {"count": len(results), "next": None,
             "previous": None, "results": results}
        )


@extend_schema(tags=[_TAG_SOLUTION_GROUP])
class SolutionGroupViewSet(viewsets.ModelViewSet):
    queryset = SolutionGroup.objects.all()
    serializer_class = SolutionGroupSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]
    

@extend_schema(tags=[_TAG_SOLUTION])  
class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]
    

@extend_schema(tags=[_TAG_SOLUTION])
class AdvantagesViewSet(viewsets.ModelViewSet):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]
    
 
@extend_schema(tags=[_TAG_SOLUTION])    
class DignitiesViewSet(viewsets.ModelViewSet):
    queryset = Dignities.objects.all()
    serializer_class = DignitiesSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]
    

@extend_schema(tags=[_TAG_SOLUTION])
class StepsViewSet(viewsets.ModelViewSet):
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


@extend_schema(tags=[_TAG_SOLUTION_FILTRATION])
class SolutionFilterViewSet(viewsets.ModelViewSet):
    queryset = SolutionFilter.objects.all()
    serializer_class = SolutionFilterSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.CoreJSONRenderer]
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


    # переопределил метод для  реализации создания тэгов при создании фильтров
    @extend_schema(
        request=FilterSerializerSwaggerListRequest,
        responses={200: FilterSerializerSwaggerListResponse},
        description='Create a solution filter.',
        summary='Create solution filter',
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
        tags_serializer = SolutionTagSerializer(data=tags_data_with_title, many=True)
        tags_serializer.is_valid(raise_exception=True)
        tags_serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    @extend_schema(
        request=FilterSerializerSwaggerListRequest,
        responses={200: {'description': 'data updated'}},
        description='Update a solution filter.',
        summary='Update solution filter',
        )
    def update(self, request, patch_value=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        if not serializer.initial_data.get('group'):
            my_filter = SolutionFilter.objects.get(id=kwargs['pk'])
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
        SolutionTag.objects.filter(title_id=filter_id).exclude(id__in=request_tags).delete()

        for tag_data in serializer.initial_data.get('tags'):
            tag_id = tag_data.get('id')
            if tag_id:
                try:
                    tag = SolutionTag.objects.get(id=tag_id)
                    if tag_data.get('properties'):
                        tag.properties = tag_data.get('properties')
                    if tag_data.get('image_tag'):
                        tag.image = tag_data.get('image_tag')
                    if tag_data.get('status'):
                        tag.status = tag_data.get('status')
                    if tag_data.get('is_message'):    
                        tag.is_message = tag_data.get('is_message')
                    tag.save()
                except SolutionTag.DoesNotExist:
                    return Response("Tag does not exist", status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    filter_instance = serializer.instance
                    tag = SolutionTag.objects.create(
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
        responses={200: FilterSerializerSwaggerListResponse},
        description='A solution filter.',
        summary='A solution filter',
        )
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # код для включения тегов, принадлежащих данному фильтру
        filter_id = serializer.data['id']
        tags = SolutionTag.objects.filter(title_id=filter_id)
        tags_serializer = SolutionTagSerializer(tags, many=True)
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
        responses={200: FilterSerializerSwaggerListResponse},
        description='List a solution filters.',
        summary='List a solution filters',
        )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        # код для включения тегов принадлежащих каждому фильтру
        serialized_data = serializer.data
        for data in serialized_data:
            filter_id = data['id']
            tags = SolutionTag.objects.filter(title_id=filter_id)
            tags_serializer = SolutionTagSerializer(tags, many=True)
            list_for_OrderedDict = []
            for tag in tags_serializer.data:
                new_tag = dict(tag)
                new_tag['filter_id'] = new_tag['title']
                new_tag.pop('title')
                tag = collections.OrderedDict(new_tag)
                list_for_OrderedDict.append(tag)
            data['tags'] = list_for_OrderedDict

        return Response(serialized_data)


@extend_schema(tags=[_TAG_SOLUTION_TAG])
class SolutionTagViewSet(viewsets.ModelViewSet):
    queryset = SolutionTag.objects.all()
    serializer_class = SolutionTagSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    # вывод всех значений
    @extend_schema(
        responses={200: ResponseSerializerSwaggerListResponse},
        description='A list solution tags.',
        summary='A list solution tags',
        )
    def list(self, request):
        groups = SolutionGroup.objects.all()
        filters = SolutionFilter.objects.all()
        tags = SolutionTag.objects.all()

        results = []
        exceptions = ["Статистика", "Тарифы", "Техническая поддержка", "Уровень сложности", ]

        # формирование списка групп
        for group in groups:
            group_data = {
                "group": group.title,
                "id": group.id,
                "count": 0,
                # "is_active": group.is_active,
                "status": group.status,
                "filters": [],
            }

            # формирование списка фильтров по группам
            for solution_filter in filters.filter(group=group):
                filter_data = {
                    "filter": f"{solution_filter.title}"
                    if solution_filter.title not in exceptions
                    else "",
                    "id": solution_filter.id,
                    "image": "" if solution_filter.title in exceptions else solution_filter.image if solution_filter.image else "None",
                    "count": 0,
                    # "is_active": solution_filter.is_active,
                    "status": solution_filter.status,
                    "functionality": solution_filter.functionality,
                    "integration": solution_filter.integration,
                    "multiple": solution_filter.multiple,
                    "tags": [],
                }

                # формирование списка тэгов по фильтрам
                for tag in tags.filter(title=solution_filter):
                    tag_data = {
                        "tag": tag.properties,
                        "id": tag.id,
                        "image_tag": tag.image if tag.image else "None",
                        # "is_active": tag.is_active,
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


@extend_schema(tags=[_TAG_SOLUTION_FILTRATION],
               request=SolutionSerializerSwaggerFiltrationRequest,
               responses={
        200: SolutionSerializerSwaggerFiltrationResponse(many=True),
    },)
class SolutionFiltration(generics.CreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Получаем параметры фильтра из запроса
        title = self.request.data.get("title")
        id_tags = self.request.data.get("id_tags", [])
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

        # Условие по минимальной цене, если она есть
        if price_min:
            q &= Q(price__gte=price_min)

        # Условие по максимальной цене, если она есть
        if price_max:
            q &= Q(price__lte=price_max)

        # Фильтрация
        if sort_abc == 'a':
            solutions = self.queryset.filter(q).order_by('title')
        elif sort_abc == 'z':
            solutions = self.queryset.filter(q).order_by('-title')
        else:
            solutions = self.queryset.filter(q)
        return solutions

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page_number = self.request.data.get("page_number")  # номер страницы
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
            
            for solution_result in modified_data['results']:
                is_favorite = False
                solution = self.queryset.filter(pk=solution_result['id']).first()
                if solution:
                    if request.user.is_authenticated:
                        favorite = FavoriteSolutions.objects.filter(user=request.user) & FavoriteSolutions.objects.filter(object_id=solution_result['id'])
                        if favorite:
                            is_favorite = True
                solution_result['is_favorite'] = is_favorite
            
            return Response(modified_data)


@extend_schema(
    description='Endpoint for searching groups and filters of solutions',
    request=SolutionFilterSearchSerializer,
    responses={
        200: SolutionFilterSearchSerializerResponse(many=False),
    },
    tags=[_TAG_SOLUTION_FILTERS_SEARCH]
)
class SolutionSearch(generics.CreateAPIView):
    queryset_group = SolutionGroup.objects.all()
    queryset_filter = SolutionFilter.objects.all()
    serializer_class_group = SolutionGroupSerializer
    serializer_class_filter = SolutionFilterSerializer
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
                'group_results': get_groups_with_filters(queryset_group, SolutionFilter.objects.all()), 
                'filter_results': serialized_data_filter
            }
            }
        return Response(response_data)


@extend_schema(tags=[_TAG_SOLUTION])
class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]