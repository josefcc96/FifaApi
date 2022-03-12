from rest_framework import serializers
from .models import *
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample



@extend_schema_serializer(
    
    examples=[
        OpenApiExample(
            'Ejemplo',
            summary='Ejemplo de Equipo',
            description='Ejemplo de respuesta de la informacion base de un Equipo',
            value={
                        "id": 1,
                        "nombre": "Equipo 1",
                        "bandera": "/Banderas/Equipo_1/bandera.png",
                        "escudo": "/Escudos/Equipo_1/escudo.png"
            },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


@extend_schema_serializer(
      
    examples=[
        OpenApiExample(
            'Ejemplo',
            summary='Ejemplo de Jugador',
            description='Ejemplo de respuesta de la serializacíon de un jugador, con la informacion del equipo al que pertenece.',
            value={
                    "id": 1,
                    "equipo": {
                        "id": 1,
                        "nombre": "Equipo 1",
                        "bandera": "/Banderas/Equipo_1/bandera.png",
                        "escudo": "/Escudos/Equipo_1/escudo.png"
                    },
                    "edad": 22,
                    "nombre": "Juan",
                    "apellido": "Perez",
                    "fecha_nacimiento": "2019-08-24",
                    "posicion": "Delantero",
                    "numero": 0,
                    "titular": "true"
            },
            request_only=False, 
            response_only=True,
        ),
    ]
)
class JugadorEquipoSerializer(serializers.ModelSerializer):
    equipo = EquipoSerializer()
    edad = serializers.ReadOnlyField()
    class Meta:
        model = Jugador
        fields = '__all__'
        depht = 1



@extend_schema_serializer(

    examples=[
        OpenApiExample(
            'Ejemplo',
            summary='Ejemplo del Cuerpo Tecnico',
            description='Ejemplo de ingreso de un miembro del cuerpo Tecnico, con la informacion del equipo al que pertenece.',
            value={
                "id": 1,
                "equipo": {
                    "id": 1,
                    "nombre": "Equipo 1",
                    "bandera": "/Banderas/Equipo_1/bandera.png",
                    "escudo": "/Escudos/Equipo_1/escudo.png"
                },
                "edad": 42,
                "nombre": "Pedro",
                "apellido": "Perez",
                "fecha_nacimiento": "2019-08-24",
                "nacionalidad": "Colombiano",
                "rol": "Tecnico",

            },
            request_only=False, 
            response_only=True,
        ),
    ]
)
class TecnicoEquipoSerializer(serializers.ModelSerializer):
    equipo = EquipoSerializer()
    edad = serializers.ReadOnlyField()
    class Meta:
        model = Tecnico
        fields = '__all__'
        depht = 1


@extend_schema_serializer(
    
    examples=[
        OpenApiExample(
            'Ejemplo',
            summary='Ejemplo del Jugador',
            description='Ejemplo de Ingreso de un jugador, el campo equipo hace relacion al identificador(id) del equipo al que pertenece.',
            value={
                "id": 1,
                "equipo": 1,
                "nombre": "Juan",
                "apellido": "Perez",
                "fecha_nacimiento": "2019-08-24",
                "posicion": "Delantero",
                "numero": 0,
                "titular": "true"
            },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class JugadorSerializer(serializers.ModelSerializer):
    equipo = serializers.PrimaryKeyRelatedField(many=False, queryset=Equipo.objects.all())
    
    class Meta:
        model = Jugador
        fields = '__all__'
        depht = 1


@extend_schema_serializer(

    examples=[
        OpenApiExample(
            'Ejemplo',
            summary='Ejemplo del Cuerpo Tecnico',
            description='Ejemplo de respuesta de la serializacíon de un miembro del cuerpo Tecnico, el campo equipo hace relacion al identificador(id) del equipo al que pertenece.',
            value={
                "id": 1,
                "equipo": 1,
                "nombre": "Pedro",
                "apellido": "Perez",
                "fecha_nacimiento": "2019-08-24",
                "nacionalidad": "Colombiano",
                "rol": "Tecnico",
            },
            request_only=False, 
            response_only=True,
        ),
    ]
)
class TecnicoSerializer(serializers.ModelSerializer):
    equipo = serializers.PrimaryKeyRelatedField(many=False, queryset=Equipo.objects.all())
    class Meta:
        model = Tecnico
        fields = '__all__'
        depht = 1


@extend_schema_serializer(
    
    examples=[
        OpenApiExample(
            'Ejemplo',
            summary='Ejemplo de Equipo',
            description='Ejemplo de respuesta de la informacion base de un Equipo, Contiene la informacion serializada de los Jugadores y el cuerpo técnico.',
            value={
                    "id": 1,
                    "nombre": "Equipo 1",
                    "bandera": "/Banderas/Equipo_1/bandera.png",
                    "escudo": "/Escudos/Equipo_1/escudo.png",
                    "jugadores": [
                        {
                            "id": 1,
                            "equipo": 1,
                            "edad": 22,
                            "nombre": "Juan",
                            "apellido": "Perez",
                            "fecha_nacimiento": "2019-08-24",
                            "posicion": "Delantero",
                            "numero": 0,
                            "titular": "true"
                        }
                    ],
                    "tecnicos": [
                            {
                                "id": 1,
                                "equipo": 1,
                                "edad": 42,
                                "nombre": "Pedro",
                                "apellido": "Perez",
                                "fecha_nacimiento": "2019-08-24",
                                "nacionalidad": "Colombiano",
                                "rol": "Tecnico",
                            }
                        ],
            },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class EquipoJugadoresTecnicosSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True, read_only=True)
    tecnicos= TecnicoSerializer(many=True, read_only=True)
    class Meta:
        model = Equipo
        fields = '__all__'


