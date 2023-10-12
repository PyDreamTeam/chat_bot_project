from rest_framework import permissions

from accounts.models import Role
from platforms.models import Platform


def get_permissions(request_method):
    if request_method == "GET":
        return [permissions.AllowAny]  # Разрешить GET-запросы без авторизации
    return [
        permissions.IsAuthenticatedOrReadOnly
    ]  # Разрешить авторизованным пользователям редактировать, остальные могут только читать


class IsAdminOrSuperAdmin(permissions.BasePermission):
    VALID_ROLES = (Role.admin, Role.superadmin)

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.user_role in self.VALID_ROLES
