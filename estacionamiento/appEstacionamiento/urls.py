from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),

    # Rutas de Clientes
    path('clientes/', views.listadoClientes, name='listadoClientes'),
    path('clientes/agregar/', views.agregarCliente, name='agregarCliente'),
    path('clientes/eliminar/<int:id>/', views.eliminarCliente, name='eliminarCliente'),
    path('clientes/actualizar/<int:id>/', views.actualizarCliente, name='actualizarCliente'),

    # Rutas de Vehículos
    path('vehiculos/', views.listadoVehiculos, name='listadoVehiculos'),
    path('vehiculos/agregar/', views.agregarVehiculo, name='agregarVehiculo'),
    path('vehiculos/eliminar/<int:id>/', views.eliminarVehiculo, name='eliminarVehiculo'),
    path('vehiculos/actualizar/<int:id>/', views.actualizarVehiculo, name='actualizarVehiculo'),

    # Rutas de Reservas
    path('reservas/', views.listadoReservas, name='listadoReservas'),
    path('reservas/agregar/', views.agregarReserva, name='agregarReserva'),
    path('reservas/eliminar/<int:id>/', views.eliminarReserva, name='eliminarReserva'),
    path('reservas/actualizar/<int:id>/', views.actualizarReserva, name='actualizarReserva'),
]
