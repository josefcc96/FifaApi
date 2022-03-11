from .models import *
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Max, Min, Avg, Count,Q

class EquipoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing teams instances.
    """
    serializer_class = EquipoJugadoresTecnicosSerializer
    queryset = Equipo.objects.all()


class JugadorViewSet(viewsets.ViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return JugadorEquipoSerializer
        return self.serializer_class
    
    def create(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = JugadorEquipoSerializer(
            Jugador.objects.get(id=serializer.data["id"]))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(Jugador.objects.all(), many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        item = get_object_or_404(Jugador.objects.all(), id=pk)
        serializer = self.get_serializer_class()
        serializer = serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = JugadorEquipoSerializer(
            Jugador.objects.get(id=serializer.data["id"]))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        item = get_object_or_404(Jugador.objects.all(), id=pk)
        serializer = self.get_serializer_class()
        serializer = serializer(item)
        return Response(serializer.data)

    def destroy(self, request,  pk=None):
        item = get_object_or_404(Jugador.objects.all(), id=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TecnicoViewSet(viewsets.ViewSet):
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TecnicoEquipoSerializer
        return self.serializer_class


    def create(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = TecnicoEquipoSerializer(
            Tecnico.objects.get(pk=serializer.data["id"]))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(self.queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer_class()
        serializer = serializer(
            item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = TecnicoEquipoSerializer(
            Tecnico.objects.get(pk=serializer.data["id"]))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer_class()
        serializer = serializer(item)
        return Response(serializer.data)

    def destroy(self, pk=None):
        item = get_object_or_404(self.queryset, id=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


@api_view(['GET'])
def report(request):
    if request.method == 'GET':
        
        response={
            'Equipos Registrados': Equipo.objects.count(),
            'Total Jugadores': Jugador.objects.count(),
            'Total Suplentes': Jugador.suplentes.all().count(),
            'Numero de Suplentes Promedio': Equipo.objects.annotate(num_suplentes=Count('jugadores', filter=Q(jugadores__titular=False))).aggregate(Avg('num_suplentes'))['num_suplentes__avg'],
            'Numero de Jugadores en promedio': Equipo.objects.annotate(num_jugadores=Count('jugadores')).aggregate(Avg('num_jugadores'))['num_jugadores__avg'],
            'Promedio Edad': Jugador.objects.promedio_edad().all().aggregate(Avg('edad_prom'))['edad_prom__avg'],
            'Equipo con mas jugadores': EquipoSerializer(Equipo.objects.annotate(num_jugadores=Count('jugadores')).order_by('-num_jugadores').first()).data,
            'Jugador mas viejo': JugadorEquipoSerializer(Jugador.objects.order_by('fecha_nacimiento').first()).data,
            'Jugador mas joven': JugadorEquipoSerializer(Jugador.objects.order_by('-fecha_nacimiento').first()).data,
            'Tecnico mas Viejo': TecnicoEquipoSerializer(Tecnico.objects.filter(rol='T').order_by('fecha_nacimiento').first()).data,
            
        }
        return Response(response)