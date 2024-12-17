# api/serializers.py

from rest_framework import serializers
from appEstacionamiento.models import ClienteEst, Vehiculo, Reserva

class ClienteEstSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteEst
        fields = '__all__'  # Esto incluirá todos los campos del modelo ClienteEst

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'  # Esto incluirá todos los campos del modelo Vehiculo

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'  # Esto incluirá todos los campos del modelo Reserva