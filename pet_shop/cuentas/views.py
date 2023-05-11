from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def login(request):
    return render(request,'cuentas/login.html')

def crearCuenta(request):
    return render(request, 'cuentas/crearCuenta.html')

def logout(request):
    logout(request)
    return render(request, 'inicio')
    