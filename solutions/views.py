from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from rest_framework import generics, permissions, renderers, status, viewsets
from rest_framework.response import Response

from .models import Solution, SolutionFilter, SolutionGroup, SolutionTag
from .serializers import (SolutionFilterSerializer, SolutionGroupSerializer,
                          SolutionSerializer, SolutionTagSerializer)
from accounts.permissions import get_permissions
from .utils import modify_data


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]

    # вывод одного значения
    def retrieve(self, request, pk=None):
        solution = self.queryset.filter(pk=pk).first()
        if solution:
            serializer = self.serializer_class(solution)
            solution_data = serializer.data
            data_solution = {
                "id": solution_data["id"],
                "title": solution_data["title"],
                "business_model": solution_data["business_model"],
                "business_area": solution_data["business_area"],
                "objective": solution_data["objective"],
                "solution_type": solution_data["business_area"],
                "short_description": solution_data["short_description"],
                "messengers": solution_data["messengers"],
                "integration_with_CRM": solution_data["integration_with_CRM"],
                "integration_with_payment_systems": solution_data["integration_with_payment_systems"],
                "actions_to_complete_tasks": solution_data["actions_to_complete_tasks"],
                "visual": solution_data["visual"],
                "price": solution_data["price"],
                "filter": solution_data["filter"],
                "is_active": solution_data["is_active"],
                "created_at": solution_data["created_at"],
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
            data_solution = {
                "id": solution_data["id"],
                "title": solution_data["title"],
                "business_model": solution_data["business_model"],
                "business_area": solution_data["business_area"],
                "objective": solution_data["objective"],
                "solution_type": solution_data["business_area"],
                "short_description": solution_data["short_description"],
                "messengers": solution_data["messengers"],
                "integration_with_CRM": solution_data["integration_with_CRM"],
                "integration_with_payment_systems": solution_data["integration_with_payment_systems"],
                "actions_to_complete_tasks": solution_data["actions_to_complete_tasks"],
                "visual": solution_data["visual"],
                "price": solution_data["price"],
                "filter": solution_data["filter"],
                "is_active": solution_data["is_active"],
                "created_at": solution_data["created_at"],
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


class SolutionGroupViewSet(viewsets.ModelViewSet):
    queryset = SolutionGroup.objects.all()
    serializer_class = SolutionGroupSerializer
    # Разрешить авторизованным пользователям редактировать, остальные могут
    # только читать
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permissions = get_permissions(self.request.method)
        return [permission() for permission in permissions]


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

    # вывод одного значения
    def retrieve(self, request, pk=None):
        solution_filter = self.queryset.filter(pk=pk).first()
        if solution_filter:
            serializer = self.serializer_class(solution_filter)
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
                {"message": "Solution filter not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    # вывод всех значений
    def list(self, request):
        groups = SolutionGroup.objects.all()
        filters = SolutionFilter.objects.all()
        SolutionTag.objects.all()

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
            for solution_filter in filters.filter(group=group):
                filter_data = {
                    "filter": solution_filter.title,
                    "id": solution_filter.id,
                    "image": f"{solution_filter.image}"
                    if solution_filter.image
                    else "None",
                    "is_active": solution_filter.is_active,
                    "functionality": solution_filter.functionality,
                    "integration": solution_filter.integration,
                    "multiple": solution_filter.multiple,
                }

                group_data["filters"].append(filter_data)
                group_data["count"] += 1

            results.append(group_data)

        return Response(
            {"count": len(results), "next": None,
             "previous": None, "results": results}
        )


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
                "is_active": group.is_active,
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
                    "is_active": solution_filter.is_active,
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
                        "image_tag": "None",  # tag.image if tag.image else "None",
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
            modified_data = modify_data(serializer.data, len(queryset))
            return Response(modified_data)