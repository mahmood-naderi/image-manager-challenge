# Django
from django.contrib import admin
from django.urls import path, include

# REST framework
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Directories
from manager.views import Save_Retrieve_Image, Search_Username, Retrieve_Image_ID

app_name = "image-manager"

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('image/', Save_Retrieve_Image.as_view(), name = 'image'),
    path('retrieve/<int:pk>/', Retrieve_Image_ID.as_view(), name = 'retrieve'),
    path('search/user/<str:username>/', Search_Username.as_view(), name = 'search'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
]
