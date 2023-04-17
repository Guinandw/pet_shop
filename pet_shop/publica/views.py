from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    lista_productos = [
        {
            'oferta':'30',
            'nombre':'Naranja',
            'precio':'120',
            'descuento':'80',
            'imagen': 'publica/images/product-1.jpg'
        },
         {
            'oferta':'0',
            'nombre':'Cebolla',
            'precio':'120',
            'descuento':'80',
            'imagen': '"{% static "publica/images/product-1.jpg" %}"'
        }
        ]
    
    context = {
                'productos': lista_productos
    }
    return render(request, 'publica/index.html', context)

def nosotros(request):
    return render(request, 'publica/about.html')

def productos(request):
    lista_productos = [
        {
            'oferta':30,
            'nombre':'Naranja',
            'precio':'120',
            'descuento':'80',
            'imagen': 'static/publica/images/product-1.jpg'
        },
         {
            'oferta':0,
            'nombre':'Mandarina',
            'precio':120,
            'descuento': None,
            'imagen': "{% static 'publica/images/product-1.jpg %}"
        }
        ]
    
    context = {
                'productos': lista_productos
    }
    return render(request, 'publica/productos.html', context)