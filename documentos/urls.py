from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_documento, name='enviar_documento'),
    path('listar/', views.listar_documentos, name='listar_documentos'),
]
