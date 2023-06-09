from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from cuentas.models import User
from .models import Favoritos

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

@login_required
def pedidos_pendientes(request):
    return render(request, 'cliente/pedidos_pendientes.html')