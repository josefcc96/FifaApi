from .views import *
from django.urls import include, re_path, path

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'equipos', EquipoViewSet)
router.register(r'jugadores', JugadorViewSet)
router.register(r'tecnicos', TecnicoViewSet)

urlpatterns = [ 
  re_path(r'^', include(router.urls)),
  path('report/', report, name='Reporte General')
]
