from rest_framework import serializers
from .models import *


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class JugadorEquipoSerializer(serializers.ModelSerializer):
    equipo = EquipoSerializer()
    edad = serializers.ReadOnlyField()
    class Meta:
        model = Jugador
        fields = '__all__'
        depht = 1


class TecnicoEquipoSerializer(serializers.ModelSerializer):
    equipo = EquipoSerializer()
    edad = serializers.ReadOnlyField()
    class Meta:
        model = Tecnico
        fields = '__all__'
        depht = 1


class JugadorSerializer(serializers.ModelSerializer):
    equipo = serializers.PrimaryKeyRelatedField(many=False, queryset=Equipo.objects.all())
    edad = serializers.ReadOnlyField()
    class Meta:
        model = Jugador
        fields = '__all__'
        depht = 1

class TecnicoSerializer(serializers.ModelSerializer):
    equipo = serializers.PrimaryKeyRelatedField(many=False, queryset=Equipo.objects.all())
    edad = serializers.ReadOnlyField()
    class Meta:
        model = Tecnico
        fields = '__all__'
        depht = 1


class EquipoJugadoresTecnicosSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True, read_only=True)
    tecnicos= TecnicoSerializer(many=True, read_only=True)
    class Meta:
        model = Equipo
        fields = '__all__'


