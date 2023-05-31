from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

# Create your views here.

class ProductoVistaList(ListView):
    model = Producto
    template_name='productos/productos.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.filter(enStock=True)
        context['titulo'] = 'Productos'
        return context
    

class ProductoVistaDetalle(ListView):
    model = Producto
    template_name = 'productos/product-single.html'
    
    def get_queryset(self):
        self.producto = get_object_or_404(Producto, pk=self.kwargs['producto_id'])
        self.productos = Producto.objects.all()
        return self.producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = self.producto
        context['titulo'] = 'Producto'
        context['productos'] = self.productos
        return context
