from django.shortcuts import render

# Create your views here.

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
        
    return render(request, 'productos/productos.html', contexto)

def producto_simple(request):
    titulo = 'Producto'
    contexto = { 'titulo' : titulo}
    return render(request, 'productos/product-single.html', contexto)
