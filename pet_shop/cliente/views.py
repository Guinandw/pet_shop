from django.shortcuts import render, redirect
from django.http import HttpResponse



# Create your views here.

def favoritos(request):
    titulo = 'Favoritos'
    contexto = { 'titulo' : titulo}
    return render(request, 'cliente/favoritos.html', contexto)


def pedidos_pendientes(request):
    return render(request, 'cliente/pedidos_pendientes.html')