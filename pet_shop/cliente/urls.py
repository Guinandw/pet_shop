from django.urls import path
from . import views

urlpatterns = {
    
    path('checkout', views.checkout, name='checkout'),
    path('registro', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('pedidos_pendientes', views.pedidos_pendientes, name='pendientes')
    
}