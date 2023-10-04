from django.contrib.contenttypes.models import ContentType
from .models import FavoritePlatforms, FavoriteSolutions
from requests import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response



class ManageFavoritePlatforms:
    @action(
      detail=True,
      methods=['get'],
      url_path='mixin_favorite',
      permission_classes=[IsAuthenticated, ]
    )
    def favorite(self, request, pk):
        instance = self.get_object()
        content_type = ContentType.objects.get_for_model(instance)
        if len(FavoritePlatforms.objects.filter(user=request.user)) <= 19:

            favorite_obj, created = FavoritePlatforms.objects.get_or_create(
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


class ManageFavoriteSolutions:
    @action(
      detail=True,
      methods=['get'],
      url_path='mixin_favorite',
      permission_classes=[IsAuthenticated, ]
    )
    def favorite(self, request, pk):
        instance = self.get_object()
        content_type = ContentType.objects.get_for_model(instance)
        if len(FavoriteSolutions.objects.filter(user=request.user)) <= 19:

            favorite_obj, created = FavoriteSolutions.objects.get_or_create(
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
