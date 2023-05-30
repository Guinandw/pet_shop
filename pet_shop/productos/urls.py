from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('product_single/', views.producto_simple, name='producto_simple'),
]
