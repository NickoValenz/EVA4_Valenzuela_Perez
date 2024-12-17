from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteEstViewSet, VehiculoViewSet, ReservaViewSet

# Crea un router
router = DefaultRouter()
router.register(r'clientes', ClienteEstViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'reservas', ReservaViewSet)

# Incluye las rutas del router
urlpatterns = [
    path('', include(router.urls)),  # Esto expone automáticamente todas las rutas CRUD
]