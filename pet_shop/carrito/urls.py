from django.urls import path
from . import views

urlpatterns = [
    
    path('carrito', views.tienda, name='carrito'),
    path('checkout', views.checkout, name='checkout'),
]