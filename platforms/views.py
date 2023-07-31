from django.db.models import Q
from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.response import Response

from .models import (Platform, PlatformFilter, PlatformGroup, PlatformImage,
                     PlatformTag)
from .serializers import (PlatformFilterSerializer, PlatformGroupSerializer,
                          PlatformImageSerializer, PlatformSerializer,
                          PlatformTagSerializer)
from .utils import get_permissions


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
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
            {"count": len(results), "next": None, "previous": None, "results": results}
        )


class PlatformGroupViewSet(viewsets.ModelViewSet):
    queryset = PlatformGroup.objects.all()
    serializer_class = PlatformGroupSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


class PlatformFilterViewSet(viewsets.ModelViewSet):
    queryset = PlatformFilter.objects.all()
    serializer_class = PlatformFilterSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.CoreJSONRenderer]
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
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
            {"count": len(results), "next": None, "previous": None, "results": results}
        )


class PlatformTagViewSet(viewsets.ModelViewSet):
    queryset = PlatformTag.objects.all()
    serializer_class = PlatformTagSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
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
                        "is_active": tag.is_active,
                        "is_message": tag.is_message,
                    }
                    filter_data["tags"].append(tag_data)
                    filter_data["count"] += 1

                group_data["filters"].append(filter_data)
                group_data["count"] += 1

            results.append(group_data)

        return Response(
            {"count": len(results), "next": None, "previous": None, "results": results}
        )


class PlatformImageViewSet(viewsets.ModelViewSet):
    queryset = PlatformImage.objects.all()
    serializer_class = PlatformImageSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


class PlatformFiltration(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    def get_queryset(self):
        # Получаем параметры фильтра из запроса
        id_tags = self.request.data.get("id_tags", [])
        price_min = self.request.data.get("price_min")
        price_max = self.request.data.get("price_max")

        # объект Q для хранения условий фильтрации
        q = Q()

        # условие по тегам, если они есть
        if id_tags:
            q &= Q(filter__id__in=id_tags)

        # условие по минимальной цене, если она есть
        if price_min:
            q &= Q(price__gte=price_min)

        # условие по максимальной цене, если она есть
        if price_max:
            q &= Q(price__lte=price_max)

        # фильтрация
        platforms = self.queryset.filter(q)

        return platforms

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.serializer_class(queryset, many=True)
        modified_data = self.modify_data(serialized_data.data)  # редактировать данные
        return Response(modified_data)

    def modify_data(self, data):
        # редактировать данные
        modified_data = []

        for item in data:
            modified_item = dict(item)
            data_my = {
                "id": modified_item["id"],
                "title": modified_item["title"],
                "short_description": modified_item["short_description"],
                "full_description": modified_item["full_description"],
                "turnkey_solutions": modified_item["turnkey_solutions"],
                "price": modified_item["price"],
                "is_active": modified_item["is_active"],
                "created_at": modified_item["created_at"],
                "image": modified_item["image"] if modified_item["image"] else "None",
                "tags": [],
            }

            for platform_tag in Platform.objects.get(
                id=modified_item["id"]
            ).filter.all():
                tag_data = {
                    "id": platform_tag.id,
                    "tag": platform_tag.properties,
                    "image_tag": platform_tag.image if platform_tag.image else "None",
                    "is_active": platform_tag.is_active,
                    "is_message": platform_tag.is_message,
                }

                data_my["tags"].append(tag_data)
            if data_my not in modified_data:
                modified_data.append(data_my)

        return {
            "count": len(modified_data),
            "next": None,
            "previous": None,
            "results": modified_data,
        }




class PlatformSearch(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    def get_queryset(self):
        title = self.request.data.get('title')
        return self.queryset.filter(title__icontains=title)