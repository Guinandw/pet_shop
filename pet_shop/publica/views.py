from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def inicio(request):
   
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/about.html')


@login_required
def productos(request):
    lista_productos = [
        {
            'oferta':30,
            'nombre':'Naranja',
            'precio':'120',
            'descuento':'80',
            'imagen': 'product-1.jpg'
        },
         {
            'oferta':0,
            'nombre':'Mandarina',
            'precio':120,
            'descuento': None,
            'imagen': 'product-2.jpg'
        }
        ]
    
    context = {
                'productos': lista_productos
    }
    return render(request, 'publica/productos.html', context)


def exit(request):
    logout(request)
    return redirect('inicio')


def blog(request):
    return render(request, 'publica/blog.html')

def blog_single(request):
    return render(request, 'publica/blog-single.html')

def contactanos(request):
    return render(request, 'publica/contacto.html')

def carrito(request):
    return render(request, 'publica/cart.html')

def checkout(request):
    return render(request, 'publica/checkout.html')

def favoritos(request):
    return render(request, 'publica/favoritos.html')

def producto_simple(request):
    return render(request, 'publica/product-single.html')