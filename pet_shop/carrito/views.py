from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string

from .carrito import Carrito
from . import body as Body
from productos.models import Producto
from .models import Orden, Orden_detalle
from cuentas.models import Perfil
from carrito.forms import EnviosForms

from django.utils import timezone, dateformat
from django.conf import settings

from . import context_processor

from django.core.mail import send_mail

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
    print(carrito.__dict__)
    
    perfil = Perfil.objects.get(pk = request.user.id)
    total = context_processor.total_carrito(request)
    orden = Orden()
    titulo = 'Chequeo de Compra'
    t = dateformat.format(timezone.now(), 'Y-m-d H:i' )
  
    print(t)
    
    
    if(request.method=='POST'):
        envio = EnviosForms(request.POST)
        
        if envio.is_valid():
            #actualizo los datos con lo que llega del post, tomando en cuenta que el cliente
            #puede cambiar los datos del envio.
            orden.nombre = request.POST['nombre']
            orden.apellido = request.POST['apellido']
            orden.direccion = request.POST['direccion']
            orden.ciudad = request.POST['ciudad']
            orden.cp = request.POST['cp']
            orden.telefono = request.POST['telefono']
            orden.fecha = t
            orden.total = total['total_carrito']
            orden.cliente = request.user
            
            
            
            orden.save()
            body = Body.encabezado(orden)
            #orden_detalle = Orden_detalle()
            for key, value in carrito.session['carrito'].items():
                orden_detalle = Orden_detalle() #para que grabe un registro por cada producto que tiene la orden, se debe crear un objeto nuevo, sino hace un UPDATE.
                orden_detalle.cantidad = value['cantidad']
                orden_detalle.descuento = 0  #el descuento no se implementó
                orden_detalle.precio_unitario = value["valor"]
                orden_detalle.subtotal = value['subtotal']
                orden_detalle.orden = orden
                orden_detalle.producto = Producto.objects.get(pk=value['producto_id'])
                orden_detalle.save()
                body = Body.agg_detalle(orden_detalle, body)
            body = Body.agg_finalbody(body)
            send_mail(
                subject='RECEPCIÓN DE PEDIDO PENDIENTE',
                message='Hemos recibido su solicitud',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[orden.cliente.email],
                html_message=render_to_string(template_name='cliente/pedidos_detalles_email.html', context={'orden': orden, 'detalles':Orden_detalle.objects.filter(orden = orden)})
                
                
                      )    
            carrito.limpiar()    
            messages.success(request,'Hemos recibido tu solicitud.')
            return redirect('carrito')
        else:
            messages.warning(request, 'Por favor verificar los datos')

    else:
        
        orden.nombre = request.user.first_name
        orden.apellido = request.user.last_name
        orden.direccion = perfil.direccion
        orden.ciudad = perfil.ciudad
        orden.cp = perfil.cp
        orden.telefono = perfil.telefono
        envio = EnviosForms(instance=orden)
        envio.save(commit=False)
        
    contexto = { 'titulo' : titulo, 'enviosForm':envio, 'carrito':carrito}
    return render(request, 'carrito/checkout.html', contexto)

        

