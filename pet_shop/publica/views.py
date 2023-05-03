from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from publica.forms import ContactanosForms
from publica.forms import EnviosForms
from publica.forms import AltasForms
from django.contrib import messages

# Create your views here.
def inicio(request):
    titulo = 'Pet Shop'
    contexto = { 'titulo' : titulo}
   
    return render(request, 'publica/index.html', contexto)

def nosotros(request):
    titulo = 'Nosotros'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/about.html', contexto)


#@login_required
def productos(request):
    lista_productos = [
        {
            'categoria': 'frutas',
            'oferta':30,
            'nombre':'Naranja',
            'precio':'120',
            'descuento':'80',
            'imagen': 'product-1.jpg'
        },
         {
             'categoria': 'frutas',
            'oferta':0,
            'nombre':'Mandarina',
            'precio':120,
            'descuento': None,
            'imagen': 'product-2.jpg'
        }
        ]
    titulo = 'Productos'
    contexto = { 'titulo' : titulo, 'productos': lista_productos}
        
    return render(request, 'publica/productos.html', contexto)


def exit(request):
    logout(request)
    return redirect('inicio')


def blog(request):
    titulo = 'Blog de Novedades'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/blog.html', contexto)

def blog_single(request):
    titulo = 'Blog de Novedades'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/blog-single.html', contexto)

def contactanos(request):
    titulo = 'Contactanos'
    if(request.method=='POST'):
        contacto_form = ContactanosForms(request.POST)
        
        if(contacto_form.is_valid()):
            messages.success('Hemos recibido tus datos')
        else:  
            messages.warning(request, 'Por favor verificar los datos')
    else:
        contacto_form= ContactanosForms()
            
    
    
    contexto = { 
                'titulo' : titulo,
                'contacto_form': contacto_form
                }
    return render(request, 'publica/contacto.html', contexto)

def carrito(request):
    titulo = 'Carrito de Compras'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/cart.html', contexto)

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
    return render(request, 'publica/checkout.html', contexto)

def favoritos(request):
    titulo = 'Favoritos'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/favoritos.html', contexto)

def producto_simple(request):
    titulo = 'Producto'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/product-single.html', contexto)

def registro(request):
    titulo = "Registrarse"
    if(request.method=='POST'):
        alta = AltasForms(request.POST)
        for i in alta:
            print(i)
        if alta.is_valid():
            messages.success(request, "Hemos recibido sus datos")
        else:
            messages.warning(request, "Por favor, ingrese todos los datos correctamente.")
    else:
        alta = AltasForms()
    contexto = { 'titulo' : titulo, 'alta':alta}
    return render(request, 'publica/registro.html', contexto)