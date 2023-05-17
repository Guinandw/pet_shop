from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from carrito.forms import EnviosForms

# Create your views here.

def carrito(request):
    titulo = 'Carrito de Compras'
    contexto = { 'titulo' : titulo}
    return render(request, 'carrito/cart.html', contexto)

def checkout(request):
    titulo = 'Chequeo de Compra'
    if(request.method=='POST'):
        envio = EnviosForms(request.POST)
        
        if envio.is_valid():
           
            messages.success(request,'Hemos recibido tu solicitud.')
        else:
            messages.warning(request, 'Por favor verificar los datos')
    
    else:
        envio = EnviosForms()
    
    contexto = { 'titulo' : titulo, 'enviosForm':envio}
    return render(request, 'carrito/checkout.html', contexto)

