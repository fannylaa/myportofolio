from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
]

# Tutorial 07: Django REST Framework
urlpatterns += [
    path('api/v1/', include('main.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
]
