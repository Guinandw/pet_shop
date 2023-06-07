from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoVistaList.as_view(), name='productos'),
    path('product_single/<int:producto_id>', views.ProductoVistaDetalle.as_view(), name='producto_simple'),
]
