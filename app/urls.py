from django.urls import path
from . import views

urlpatterns = [
    path("api/ejecutar/", views.ejecutar_programa, name="ejecutar_programa"),
]

