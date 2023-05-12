from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def perfil(request):
    return render(request, 'cliente/perfil.html')


def favoritos(request):
    titulo = 'Favoritos'
    contexto = { 'titulo' : titulo}
    return render(request, 'cliente/favoritos.html', contexto)

""" def registro(request):
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
    return render(request, 'cliente/registro.html', contexto) """

def pedidos_pendientes(request):
    return render(request, 'cliente/pedidos_pendientes.html')