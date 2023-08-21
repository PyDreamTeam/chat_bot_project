from rest_framework import permissions

def get_permissions(request_method):
    if request_method == "GET":
        return [permissions.AllowAny]
    return [
        permissions.IsAuthenticatedOrReadOnly
    ]
