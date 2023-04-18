from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
   
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/about.html')

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


def blog(request):
    return render(request, 'publica/blog.html')

def blog_single(request):
    return render(request, 'publica/blog-single.html')
    