from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers
from solutions.views import SolutionsViewSet


router_solution = routers.DefaultRouter()
router_solution.register(r'solution', SolutionsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('accounts.urls')),
    #drf-spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/', include(router_solution.urls))    #http://127.0.0.1:8000/api/v1/solution/



 


]