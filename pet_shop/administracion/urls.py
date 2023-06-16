from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.PedidosTotales.as_view(), name='pedidos'),
    path("stock/", views.stock , name="stock"),
    path("pedido_detalle/<int:pk>", views.PedidoDetalleView.as_view(), name='pedido_detalle'),
    path("pedido_update/<int:pk>", views.PedidoDetalleUpdate.as_view(), name='pedido_update')
    
    
]