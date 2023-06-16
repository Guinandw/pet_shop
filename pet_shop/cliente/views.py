from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from productos.models import Producto
from cuentas.models import User
from .models import Favoritos

from django.views.generic import ListView
from carrito.models import Orden, Orden_detalle

# Create your views here.
@login_required
def favoritos(request):
    favoritos = Favoritos.objects.filter(cliente = request.user)
    titulo = 'Favoritos'
    contexto = { 'titulo' : titulo, 'favoritos': favoritos}
    return render(request, 'cliente/favoritos.html', contexto)

@login_required
def agregar_favoritos(request, producto_id):
    user = User.objects.get(id=request.user.id)
    producto = Producto.objects.get(id=producto_id) 
    nuevoFavorito = Favoritos(cliente= user, producto = producto )
    nuevoFavorito.save()
    return redirect('productos')
    
@login_required
def eliminar_favoritos(request, producto_id):
    user = User.objects.get(id=request.user.id)
    producto = Producto.objects.get(id=producto_id)
    favorito = Favoritos.objects.filter(cliente = user, producto=producto)    
    favorito.delete()
    return redirect('favoritos')



class PedidosPendienteView(LoginRequiredMixin,ListView):
    model = Orden
    template_name = 'cliente/pedidos_pendientes.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['ordenes'] = Orden.objects.filter(cliente=self.request.user)
        context['titulo'] = 'ORDENES PENDIENTES'
        return context
    
class PedidosVistaDetalle(LoginRequiredMixin,ListView):
    model = Orden_detalle
    template_name = 'cliente/pedidos_pendientes_detalles.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orden"] = Orden.objects.get(pk=self.kwargs['orden_id'])
        context["detalles"] = Orden_detalle.objects.filter(orden = context["orden"])
        return context
    

class PedidosHistorialView(LoginRequiredMixin,ListView):
    model = Orden
    template_name = 'cliente/pedidos_historial.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['ordenes'] = Orden.objects.filter(cliente=self.request.user)
        context['titulo'] = 'HISTORIAL DE ORDENES'
        return context