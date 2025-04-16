from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/', views.solicitar_compra, name='solicitar_compra'),
    path('minhas/', views.minhas_solicitacoes, name='minhas_solicitacoes'),

]
