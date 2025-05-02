from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user_auth.serializers.login_and_registration_serializer.token_obtain import CustomTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="Exam Project API",
        default_version='v1',
        description="API for Exam project",
        contact=openapi.Contact(email="contact@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_auth.urls')),

    # JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
