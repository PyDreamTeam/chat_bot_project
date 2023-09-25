from django.contrib.contenttypes.models import ContentType
from .models import Favorite
from requests import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Exists, OuterRef


class ManageFavorite:
    @action(
      detail=True,
      methods=['get'],
      url_path='favorite',
      permission_classes=[IsAuthenticated, ]
    )
    def favorite(self, request, pk):
        instance = self.get_object()
        content_type = ContentType.objects.get_for_model(instance)
        if len(Favorite.objects.filter(user=request.user)) <= 19:

            favorite_obj, created = Favorite.objects.get_or_create(
                user=request.user, content_type=content_type, object_id=instance.id
            )

            if created:
                return Response(
                    {'message': 'Контент добавлен в избранное'},
                    status=status.HTTP_201_CREATED
                )
            else:
                favorite_obj.delete()
                return Response(
                    {'message': 'Контент удален из избранного'},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {'message': 'Достигнут предел добавления в избранное'},
                status=status.HTTP_200_OK
            )
    # def favorites(self, request):
    #     print('start1')
    #     queryset = self.get_queryset().filter(is_favorite=True)
    #     serializer_class = self.get_serializer_class()
    #     serializer = serializer_class(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    #
    # def annotate_qs_is_favorite_field(self, queryset):
    #     print('start 2')
    #
    #     if self.request.user.is_authenticated:
    #         print('start 3')
    #         is_favorite_subquery = Favorite.objects.filter(user=self.request.user)
    #         print(is_favorite_subquery)
    #         #     object_id=OuterRef('pk'),
    #         #     user=self.request.user,
    #         #
    #         #     content_type=ContentType.objects.get_for_model(queryset.model)
    #         # )
    #         # print(is_favorite_subquery)
    #
    #
    #
    #         queryset = queryset.annotate(is_favorite=Exists(is_favorite_subquery))
    #         print(queryset)
    #     return queryset

