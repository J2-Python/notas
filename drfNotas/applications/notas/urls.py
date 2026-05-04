from django.urls import path
from .views import ListaNotas
app_name="notas_app"

urlpatterns = [
    path('lista-notas/',ListaNotas.as_view(),name="notas"),
]
