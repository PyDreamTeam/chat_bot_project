from django.contrib.contenttypes.models import ContentType
from favorite.models import Favorite
from requests import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


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