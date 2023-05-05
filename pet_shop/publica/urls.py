from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros' ),
    path('productos/', views.productos, name='productos'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('product_single', views.producto_simple, name='producto_simple'),
    path('logput/', views.exit, name='exit')
]