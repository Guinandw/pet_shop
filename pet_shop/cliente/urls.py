from django.urls import path
from . import views

urlpatterns = {
    
    path('favoritos', views.favoritos, name='favoritos'),
    path('registro', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('pedidos_pendientes', views.pedidos_pendientes, name='pendientes')
    
}