from rest_framework import permissions

from platforms.models import Platform


def get_permissions(request_method):
    if request_method == "GET":
        return [permissions.AllowAny]  # Разрешить GET-запросы без авторизации
    return [
        permissions.IsAuthenticatedOrReadOnly
    ]  # Разрешить авторизованным пользователям редактировать, остальные могут только читать
