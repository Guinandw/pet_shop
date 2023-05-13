from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import userFormCompleto 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request,'cuentas/login.html')
    form = forms.userFormCompleto



def crearCuenta(request):
    if request.method == 'GET':
        
        return render(request, 'cuentas/crearCuenta.html', {'titulo':'Registrarse','form': userFormCompleto})
    else:
        usuario = request.POST['username']    
        nombre = request.POST['first_name'] 
        apellido = request.POST['last_name']  
        email = request.POST['email']   
        password1 = request.POST['password1']  
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create(username = usuario, password = password1, first_name = nombre,
                                           last_name = apellido, email = email
                                           )
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'crearCuenta.html', {'form':userFormCompleto} )
@login_required          
def salir(request):
    logout(request)
    return render(request, 'inicio')
    
def inicioSesion(request):
    titulo = 'Inicio Sesion'
    if request.method == 'GET':
        return render(request, 'inicioSesion.html', {'form':AuthenticationForm, 'titulo':titulo})
    else:
        usuario = authenticate(request, 
                                   username=request.POST['username'], 
                                   password = request.POST['password']
                                   )
        if usuario is None:
            return render(request, 'inicioSesion.html', 
                          {'form':AuthenticationForm, 
                           'titulo':titulo, 
                           'error':'Usuario o password incorrecto'})
        else:
            login(request, usuario)
            return render('inicio')

def perfil(request, user_id):
      pass