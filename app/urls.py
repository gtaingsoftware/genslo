from django.urls import path
from . import views

urlpatterns = [
    path('api/generar-kml/', views.generar_kml, name='generar_kml'),
    path('api/generar-txt/', views.generar_txt, name='generar_txt'),
]
