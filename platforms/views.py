from django.db.models import Q
from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.response import Response

from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag
from .serializers import (PlatformFilterSerializer, PlatformGroupSerializer,
                          PlatformSerializer, PlatformTagSerializer)
from .permissions import get_permissions
from .utils import modify_data


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    # вывод одного значения
    def retrieve(self, request, pk=None):
        platform = self.queryset.filter(pk=pk).first()
        if platform:
            serializer = self.serializer_class(platform)
            platform_data = serializer.data
            data_platform = {
                "id": platform_data["id"],
                "title": platform_data["title"],
                "short_description": platform_data["short_description"],
                "full_description": platform_data["full_description"],
                "turnkey_solutions": platform_data["turnkey_solutions"],
                "price": platform_data["price"],
                "is_active": platform_data["is_active"],
                "created_at": platform_data["created_at"],
                "image": platform_data["image"] if platform_data["image"] else "None",
                "tags": [],
            }

            for platform_tag in platform.filter.all():
                tag_data = {
                    "id": platform_tag.id,
                    "tag": platform_tag.properties,
                    "image_tag": platform_tag.image if platform_tag.image else "None",
                    "is_active": platform_tag.is_active,
                    "is_message": platform_tag.is_message,
                }

                data_platform["tags"].append(tag_data)

            return Response(data_platform)
        else:
            return Response(
                {"message": "Platform not found."}, status=status.HTTP_404_NOT_FOUND
            )

    # вывод всех значений

    def list(self, request):
        platforms = Platform.objects.all()

        results = []

        # формирование списка групп
        for platform in platforms:
            serializer = self.serializer_class(platform)
            platform_data = serializer.data
            data_platform = {
                "id": platform_data["id"],
                "title": platform_data["title"],
                "short_description": platform_data["short_description"],
                "full_description": platform_data["full_description"],
                "turnkey_solutions": platform_data["turnkey_solutions"],
                "price": platform_data["price"],
                "is_active": platform_data["is_active"],
                "created_at": platform_data["created_at"],
                "image": platform_data["image"] if platform_data["image"] else "None",
                "tags": [],
            }

            for platform_tag in platform.filter.all():
                tag_data = {
                    "id": platform_tag.id,
                    "tag": platform_tag.properties,
                    "image_tag": platform_tag.image if platform_tag.image else "None",
                    "is_active": platform_tag.is_active,
                    "is_message": platform_tag.is_message,
                }

                data_platform["tags"].append(tag_data)

            results.append(data_platform)

        return Response(
            {"count": len(results), "next": None,
             "previous": None, "results": results}
        )


class PlatformGroupViewSet(viewsets.ModelViewSet):
    queryset = PlatformGroup.objects.all()
    serializer_class = PlatformGroupSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


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

    # вывод одного значения
    def retrieve(self, request, pk=None):
        platform_filter = self.queryset.filter(pk=pk).first()
        if platform_filter:
            serializer = self.serializer_class(platform_filter)
            filter_data = dict(serializer.data)
            return Response(
                {
                    "filter": filter_data["title"],
                    "id": filter_data["id"],
                    "image": f"{filter_data['image']}"
                    if filter_data["image"]
                    else "None",
                    "is_active": filter_data["is_active"],
                    "group": filter_data["group"],
                    "functionality": filter_data["functionality"],
                    "integration": filter_data["integration"],
                    "multiple": filter_data["multiple"],
                }
            )
        else:
            return Response(
                {"message": "Platform filter not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    # вывод всех значений
    def list(self, request):
        groups = PlatformGroup.objects.all()
        filters = PlatformFilter.objects.all()
        PlatformTag.objects.all()

        results = []

        # формирование списка групп
        for group in groups:
            group_data = {
                "group": group.title,
                "id": group.id,
                "count": 0,
                "is_active": group.is_active,
                "filters": [],
            }

            # формирование списка фильтров по группам
            for platform_filter in filters.filter(group=group):
                filter_data = {
                    "filter": platform_filter.title,
                    "id": platform_filter.id,
                    "image": f"{platform_filter.image}"
                    if platform_filter.image
                    else "None",
                    "is_active": platform_filter.is_active,
                    "functionality": platform_filter.functionality,
                    "integration": platform_filter.integration,
                    "multiple": platform_filter.multiple,
                }

                group_data["filters"].append(filter_data)
                group_data["count"] += 1

            results.append(group_data)

        return Response(
            {"count": len(results), "next": None,
             "previous": None, "results": results}
        )


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
                "is_active": group.is_active,
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
                    "is_active": platform_filter.is_active,
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
                        "image_tag": "None",#tag.image if tag.image else "None",
                        "is_active": tag.is_active,
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


class PlatformFiltration(generics.CreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
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
            platforms = self.queryset.filter(q).order_by('title')
        elif sort_abc == 'z':
            platforms = self.queryset.filter(q).order_by('-title')
        else:
            platforms = self.queryset.filter(q)
        return platforms

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.serializer_class(queryset, many=True)
        modified_data = modify_data(serialized_data.data)
        return Response(modified_data)


# class PlatformSearch(generics.ListAPIView):
#     queryset = Platform.objects.all()
#     serializer_class = PlatformSerializer
#     # Разрешить авторизованным пользователям редактировать, остальные могут
#     # только читать
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_permissions(self):
#         permissions = get_permissions(self.request.method)
#         return [permission() for permission in permissions]

#     def get_queryset(self):
#         title = self.request.data.get("title")
#         return self.queryset.filter(title__icontains=title)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serialized_data = self.serializer_class(queryset, many=True)
#         modified_data = modify_data(serialized_data.data)
#         return Response(modified_data)
