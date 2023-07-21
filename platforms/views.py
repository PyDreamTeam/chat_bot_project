from rest_framework import viewsets
from rest_framework.response import Response

from .models import Platform, PlatformFilter, PlatformGroup, PlatformTag
from .serializers import (PlatformFilterSerializer, PlatformGroupSerializer,
                          PlatformSerializer, PlatformTagSerializer)


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformGroupViewSet(viewsets.ModelViewSet):
    queryset = PlatformGroup.objects.all()
    serializer_class = PlatformGroupSerializer


class PlatformFilterViewSet(viewsets.ModelViewSet):
    queryset = PlatformFilter.objects.all()
    serializer_class = PlatformFilterSerializer

    def list(self, request):
        groups = PlatformGroup.objects.all()
        filters = PlatformFilter.objects.all()
        tags = PlatformTag.objects.all()

        results = []

        for group in groups:
            group_data = {
                "group": group.title,
                "id": group.id,
                "count": 0,
                "is_active": group.is_active,
                "filters": [],
            }

            for platform_filter in filters.filter(group=group):
                filter_data = {
                    "filter": platform_filter.title,
                    "id": platform_filter.id,
                    # "image": platform_filter.image,
                    "is_active": platform_filter.is_active,
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

    def list(self, request):
        groups = PlatformGroup.objects.all()
        filters = PlatformFilter.objects.all()
        tags = PlatformTag.objects.all()

        results = []

        for group in groups:
            group_data = {
                "group": group.title,
                "id": group.id,
                "count": 0,
                "is_active": group.is_active,
                "filters": [],
            }

            for platform_filter in filters.filter(group=group):
                filter_data = {
                    "filter": platform_filter.title,
                    "id": platform_filter.id,
                    # "image": platform_filter.image,
                    "count": 0,
                    "is_active": platform_filter.is_active,
                    "tags": [],
                }

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


# class PlatformViewSet(viewsets.ModelViewSet):
#     queryset = Platform.objects.all()
#     serializer_class = PlatformSerializer

# class PlatformGroupViewSet(viewsets.ModelViewSet):
#     queryset = PlatformGroup.objects.all()
#     serializer_class = PlatformGroupSerializer

# class PlatformFilterViewSet(viewsets.ModelViewSet):
#     queryset = PlatformFilter.objects.all()
#     serializer_class = PlatformFilterSerializer

# class PlatformTagViewSet(viewsets.ModelViewSet):
#     queryset = PlatformTag.objects.all()
#     serializer_class = PlatformTagSerializer

#     def list(self, request):
#         queryset = PlatformTag.objects.all()
#         serializer = PlatformTagSerializer(queryset, many=True)
#         filters_list = serializer.data
#         results = []
#         filters = []
#         # Выборка и формирование всех групп
#         for group_item in filters_list:

#             for filter_item in filters_list:
#                 tags = []
#                 # выборка и формирование всех тэгов для фильтров
#                 for item in filters_list:
#                     tag_filter = {}
#                     tag_filter = {"id": item["id"], "properties": item["properties"], "is_active": item["is_active"]}
#                     if item['title'] == filter_item["title"]:
#                         tags.append(tag_filter)
#                 # создаие фильтра
#                 platform_filter = {
#                             "title": filter_item["title"],
#                             "image": filter_item["image"],
#                             "count": len(tags),
#                             "tags": tags,
#                         }
#                 # проверка наличия фильтра в фильтрах группы (если уже добавлен, то не добавлять)
#                 has_filter = False
#                 for item in filters:
#                     if item['title'] == filter_item["title"]:
#                         has_filter = True
#                         break
#                 if not has_filter:
#                     filters.append(platform_filter)

#             # создаие фильтра
#             groups_of_filter = {
#                             "group": group_item["group"],
#                             "count": len(filters),
#                             "filters": filters,
#             }
#             # проверка наличия группы в результатах (если уже добавлен, то не добавлять)
#             has_group = False
#             for item in results:
#                 if item['group'] == group_item["group"]:
#                     has_group = True
#                     break
#             if not has_group:
#                 results.append(groups_of_filter)


#         return Response({
#             "count": len(results),
#             "next": None,
#             "previous": None,
#             "results": results
#         })


# def list(self, request):
#     queryset = PlatformFilter.objects.all()
#     serializer = PlatformFilterSerializer(queryset, many=True)
#     filters_list = serializer.data
#     results = []
#     # Выборка и формирование всех фильтров
#     for filter_item in filters_list:
#         tags = []
#         # выборка и формирование всех тэгов для фильтров
#         for item in filters_list:
#             tag_filter = {}
#             tag_filter = {"id": item["id"], "properties": item["properties"], "is_active": item["is_active"]}
#             if item['title'] == filter_item["title"]:
#                 tags.append(tag_filter)
#         # создаие фильтра
#         platform_filter = {
#                     "title": filter_item["title"],
#                     "group": filter_item["group"],
#                     "image": filter_item["image"],
#                     "tags": tags,
#                 }
#         # проверка наличия фильтра в результатах (если уже добавлен, тоне добпять)
#         has_filter = False
#         for item in results:
#             if item['title'] == filter_item["title"]:
#                 has_filter = True
#                 break
#         if not has_filter:
#             results.append(platform_filter)


#     return Response({
#         "count": len(results),
#         "next": None,
#         "previous": None,
#         "results": results
#     })
