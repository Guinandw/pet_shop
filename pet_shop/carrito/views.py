from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .carrito import Carrito
from productos.models import Producto

from carrito.forms import EnviosForms
from . import context_processor

# Create your views here.


@login_required
def carro(request):
    carrito = Carrito(request)
    titulo = 'Carrito de Compras'
    contexto = { 'titulo' : titulo, 'carrito': carrito}
    return render(request, 'carrito/carrito.html', contexto)

@login_required
def agregar_producto(request, producto_id, origen):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.agregar(producto)
    if origen == 1:
        return redirect('productos')
    elif origen == 2:
        return redirect('carrito')

@login_required
def sacar_producto(request, producto_id, origen):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.restar(producto)
    if origen == 1:
        return redirect('productos')
    elif origen == 2:
        return redirect('carrito')

@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    Carrito.limpiar(request)
    return redirect('carrito')

@login_required
def checkout(request):
    carrito = Carrito(request)
    total = context_processor.total_carrito(request)
    titulo = 'Chequeo de Compra'
    if(request.method=='POST'):
        envio = EnviosForms(request.POST)
        
        if envio.is_valid():
           
            messages.success(request,'Hemos recibido tu solicitud.')
        else:
            messages.warning(request, 'Por favor verificar los datos')
    
    else:
        envio = EnviosForms()
    
    contexto = { 'titulo' : titulo, 'enviosForm':envio, 'carrito':carrito}
    return render(request, 'carrito/checkout.html', contexto)

