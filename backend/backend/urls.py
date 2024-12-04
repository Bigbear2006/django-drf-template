from django.contrib import admin
from django.urls import include, path
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.openapi import Info
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ['https'] if request.is_secure() else ['http']
        return schema


schema_view = get_schema_view(
    Info('API', 'v1', 'API description'),
    authentication_classes=[JWTAuthentication],
    generator_class=CustomSchemaGenerator,
    permission_classes=[AllowAny],
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/', include('jwt_auth.urls')),
    path('api/docs/', schema_view.with_ui('swagger')),
]
