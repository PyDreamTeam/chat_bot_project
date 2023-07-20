from django.shortcuts import render
from rest_framework import viewsets
from .models import Platform, PlatformFilter
from .serializers import PlatformSerializer, PlatformFilterSerializer
from rest_framework.response import Response

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformFilterViewSet(viewsets.ModelViewSet):
    queryset = PlatformFilter.objects.all()
    serializer_class = PlatformFilterSerializer

    def list(self, request):
        queryset = PlatformFilter.objects.all()
        serializer = PlatformFilterSerializer(queryset, many=True)
        filters_list = serializer.data
        results = []
        # Выборка и формирование всех фильтров
        for filter_item in filters_list:
            tags = []
            # выборка и формирование всех тэгов для фильтров
            for item in filters_list:
                tag_filter = {}
                tag_filter = {"id": item["id"], "properties": item["properties"], "is_active": item["is_active"]}
                if item['title'] == filter_item["title"]:
                    tags.append(tag_filter)
            # создаие фильтра
            platform_filter = {
                        "title": filter_item["title"],
                        "functionality": filter_item["functionality"],
                        "integration": filter_item["integration"],
                        "image": filter_item["image"],
                        "tags": tags,
                    }
            # проверка наличия фильтра в результатах (если уже добавлен, тоне добпять)
            has_filter = False
            for item in results:
                if item['title'] == filter_item["title"]:
                    has_filter = True
                    break
            if not has_filter:
                results.append(platform_filter)

               
        return Response({
            "count": len(results),
            "next": None,
            "previous": None,
            "results": results
        })