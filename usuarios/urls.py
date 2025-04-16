from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
]