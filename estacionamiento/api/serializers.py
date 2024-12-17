
from rest_framework import serializers
from appEstacionamiento.models import ClienteEst, Vehiculo, Reserva

class ClienteEstSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteEst
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'