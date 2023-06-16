from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from carrito.models import Orden, Orden_detalle

# Create your views here.
def pedidos(request):
    return render(request, 'administracion/pedidos.html')

def stock(request):
    return render(request, 'administracion/stock.html')

class PedidosTotales(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Orden
    template_name = 'administracion/pedidos.html'
    permission_required = 'administrador'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['ordenes'] = Orden.objects.all()
        context['titulo'] = 'ORDENES PENDIENTES'
        return context



class PedidoDetalleView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Orden_detalle
    template_name = 'administracion/pedido_detalle.html'
    permission_required = 'administrador'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orden"] = Orden.objects.get(pk=self.kwargs['pk'])
        context["detalles"] = Orden_detalle.objects.filter(orden = context["orden"])
        context['titulo'] = 'DETALLE ORDEN'
        return context
    
class PedidoDetalleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Orden
    template_name = 'administracion/pedido_update.html'
    fields = ['no_factura', 'estado', ]
    success_url = reverse_lazy('pedidos')
    permission_required = 'administrador'
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context['orden'] = Orden.objects.get(pk=pk)
        context['titulo'] = 'EDITAR ORDEN'
        return context
    
    