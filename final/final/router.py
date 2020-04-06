from Personas.viewsets import PersonasViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', PersonasViewSet)
