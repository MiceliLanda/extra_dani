from rest_framework import routers, serializers, viewsets
from .models import ModelRegistro

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelRegistro
        fields = ('__all__')

