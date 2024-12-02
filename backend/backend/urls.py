from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info

view = get_schema_view(Info("API", "v1", "API description"), public=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('api/auth/', include("jwt_auth.urls")),
    path('api/docs/', view.with_ui("swagger")),
]

if not settings.DOCKER:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
