from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteEstViewSet, VehiculoViewSet, ReservaViewSet

#crea un router
router = DefaultRouter()
router.register(r'clientes', ClienteEstViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'reservas', ReservaViewSet)

#incluye las rutas del router
urlpatterns = [
    path('', include(router.urls)),  #muestra el Crud
]