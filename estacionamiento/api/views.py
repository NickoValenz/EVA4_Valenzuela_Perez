from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from appEstacionamiento.models import ClienteEst, Vehiculo, Reserva
from .serializers import ClienteEstSerializer, VehiculoSerializer, ReservaSerializer

class ClienteEstViewSet(viewsets.ModelViewSet):
    queryset = ClienteEst.objects.all()
    serializer_class = ClienteEstSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer