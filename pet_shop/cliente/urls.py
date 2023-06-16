from django.urls import path
from . import views

urlpatterns = [
    
    path('favoritos/', views.favoritos, name='favoritos'),
    path('agregar_favoritos/<int:producto_id>/', views.agregar_favoritos, name='agregar_favoritos'),
    path('eliminar_favoritos/<int:producto_id>/', views.eliminar_favoritos, name='eliminar_favoritos'),
    path('pedidos_pendientes/', views.PedidosPendienteView.as_view(), name='pendientes'),
    path('pedidos_pendientes_detalle/<int:orden_id>', views.PedidosVistaDetalle.as_view(), name='pendiente_detalle'),
    path('pedidos_historial/', views.PedidosHistorialView.as_view(), name='historial'),
    
]