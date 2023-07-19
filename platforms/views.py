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
        for filter_item in filters_list:
            
            platform_filter = {
                "id": filter_item["id"],
                "properties": filter_item["properties"],
                "is_active": filter_item["is_active"]
            }
            print(filter_item, '*******************************************')
            try:
                platform = Platform.objects.filter(filter__id=filter_item["id"])[0]
                platform_serializer = PlatformSerializer(platform)
                platform_data = platform_serializer.data
                platform_filter.update({
                    "title": platform_data["title"],
                    "functionality": platform_data["functionality"],
                    "integration": platform_data["integration"],
                    "image": platform_data["image"]
                })
            except IndexError:
                pass
            results.append(platform_filter)
            # print(results, '------------------------------------------------------------------------+')
        return Response({
            "count": len(results),
            "next": None,
            "previous": None,
            "results": results
        })