from django.urls import path
from . import views

urlpatterns = [
    
    path('carrito', views.carro, name='carrito'),
    path('checkout', views.checkout, name='checkout'),
    path('agregar/<int:producto_id>/<int:origen>', views.agregar_producto, name='agregar_producto'),
    path('restar/<int:producto_id>/<int:origen>', views.sacar_producto, name='sacar_producto'),
    path('eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito')
]