from rest_framework import viewsets, status, renderers, permissions
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response

from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag
from .serializers import (PlatformFilterSerializer, PlatformGroupSerializer,
                          PlatformSerializer, PlatformTagSerializer)


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Разрешить авторизованным пользователям редактировать, остальные могут только читать

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]  # Разрешить GET-запросы без авторизации
        return super().get_permissions()


class PlatformGroupViewSet(viewsets.ModelViewSet):
    queryset = PlatformGroup.objects.all()
    serializer_class = PlatformGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Разрешить авторизованным пользователям редактировать, остальные могут только читать

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]  # Разрешить GET-запросы без авторизации
        return super().get_permissions()


class PlatformFilterViewSet(viewsets.ModelViewSet):
    queryset = PlatformFilter.objects.all()
    serializer_class = PlatformFilterSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.CoreJSONRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Разрешить авторизованным пользователям редактировать, остальные могут только читать

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]  # Разрешить GET-запросы без авторизации
        return super().get_permissions()

    # вывод одного значения
    def retrieve(self, request, pk=None):
        platform_filter = self.queryset.filter(pk=pk).first()
        if platform_filter:
            serializer = self.serializer_class(platform_filter)
            filter_data = dict(serializer.data)
            return Response({
                    "filter": filter_data['title'],
                    "id": filter_data['id'],
                    "image": f"{filter_data['image']}" if filter_data['image'] else 'None',
                    "is_active": filter_data['is_active'],
                    "group": filter_data['group'],
                    "functionality": filter_data['functionality'],
                    "integration": filter_data['integration'],
                })
        else:
            return Response({"message": "Platform filter not found."}, status=status.HTTP_404_NOT_FOUND)

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
                    "image": f"{platform_filter.image}" if platform_filter.image else 'None',
                    "is_active": platform_filter.is_active,
                    "functionality": platform_filter.functionality,
                    "integration": platform_filter.integration,
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Разрешить авторизованным пользователям редактировать, остальные могут только читать

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]  # Разрешить GET-запросы без авторизации
        return super().get_permissions()

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
                    "image": f"{platform_filter.image}" if platform_filter.image else 'None',
                    "count": 0,
                    "is_active": platform_filter.is_active,
                    "functionality": platform_filter.functionality,
                    "integration": platform_filter.integration,
                    "tags": [],
                }

                # формирование списка тэгов по фильтрам
                for tag in tags.filter(title=platform_filter):
                    tag_data = {
                        "tag": tag.properties,
                        "id": tag.id,
                        "is_active": tag.is_active,
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
