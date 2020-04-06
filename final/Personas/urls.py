from django.urls import path, re_path
from django.conf.urls import include,url
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from Personas import views
from Personas.views import CustonAuthToken

urlpatterns = [
    url(r'personas/',views.lista_personas),  
]
