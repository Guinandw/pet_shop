from django.urls import path
from . import views

urlpatterns = [
    
    path('favoritos', views.favoritos, name='favoritos'),
    path('pedidos_pendientes', views.pedidos_pendientes, name='pendientes')
    
]