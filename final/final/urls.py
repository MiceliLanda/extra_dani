
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from Personas.views import CustonAuthToken

urlpatterns = [
    path(r'admin/', admin.site.urls),
     url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^',include('Personas.urls')),
]
