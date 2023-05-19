from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from .forms import userFormCompleto, PerfilForm, editarUsuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Perfil
from django.http import Http404

# Create your views here.
def crearCuenta(request):
    if request.method == 'GET':
        
        return render(request, 'cuentas/crearCuenta.html', {'titulo':'Registrarse','form': userFormCompleto()})
    else:
        userForm = userFormCompleto(request.POST)
        usuario = request.POST['username']    
        nombre = request.POST['first_name'] 
        apellido = request.POST['last_name']  
        email = request.POST['email']   
        password1 = request.POST['password1']  
        password2 = request.POST['password2']
        
        
        if userForm.is_valid():
            if password1 == password2:
                try:
                    user = User.objects.create(username = usuario, first_name = nombre,
                                            last_name = apellido, email = email
                                            )
                    user.set_password(password1)
                    user.save()
                    login(request, user)
                    return redirect('perfil')
                except IntegrityError:
                    messages.warning(request, 'Cuenta Existente')
                    return render(request, 'cuentas/crearCuenta.html', {'form':userFormCompleto(), 'errors':'Cuenta Existente'} )
            else:
                messages.warning(request, 'Confirmar Password')
                return render(request, 'cuentas/crearCuenta.html', {'form':userFormCompleto(), 'errors':'Confirmar Password.'} )
        else:
            messages.warning(request, 'Por Favor verificar los datos')
            return render(request, 'cuentas/crearCuenta.html', {'form':userForm})


@login_required          
def salir(request):
    logout(request)
    return render(request, 'publica/index.html')
    
def inicioSesion(request):
    titulo = 'Inicio Sesion'
    if request.method == 'GET':
        return render(request, 'cuentas/inicioSesion.html', {'form':AuthenticationForm, 'titulo':titulo})
    else:
        usuario = authenticate(request, 
                                   username=request.POST['username'], 
                                   password = request.POST['password']
                                   )
        print(usuario)
        if usuario is None:
            messages.warning(request, 'Usuario o password incorrecto')
            return render(request, 'cuentas/inicioSesion.html', 
                          {'form':AuthenticationForm, 
                           'titulo':titulo, 
                           })
        else:
            #messages.success(request, 'Bienvenido')
            login(request, usuario)
            return render(request, 'publica/index.html')

@login_required
def perfil(request):
    usuario = User.objects.get(pk=request.user.id)
    
    try:
        adicional = get_object_or_404(Perfil,user_id = request.user.id)
    except Http404:
        adicional = 'No ha agregado informacion adicional'
    
    if request.method == 'GET':
        return render(request, 
                      'cuentas/perfil.html', 
                      {'form':PerfilForm, 'user':usuario, 'adicional':adicional})
    
        
@login_required
def editarUsuario(request):
    usuario = User.objects.get(pk=request.user.id)

    if request.method == 'GET':
        usuarioForm = userFormCompleto(instance= usuario)
        return render(request, 
                      'cuentas/editarUsuario.html', 
                      {'form':usuarioForm})
    else:
        
        usuario.first_name = request.POST['first_name']
        usuario.last_name = request.POST['last_name']
        usuario.email = request.POST['email']        
        usuario.save()
        return redirect('perfil')
        
@login_required
def editarPerfil(request):

    try:
        perfil = get_object_or_404(Perfil,user_id = request.user.id)
        form = PerfilForm(instance=perfil)
    except Http404:
        perfil = 0
        form = PerfilForm()
    
    if request.method == 'GET':
       
        return render(request, 
                      'cuentas/editarPerfil.html', 
                      {'form':form})
    else:
            if isinstance(perfil, Perfil):
                print('dentro de isInstance')
                try:
                    form = PerfilForm(request.POST, instance=perfil)
                    perfil = form.save(commit=False)
                except ValueError:
                    messages.warning(request,'Verificar Datos')
                    return render(request, 'cuentas/editarPerfil.html', 
                      {'form':form})
                    
            else:
                try:
                    form = PerfilForm(request.POST)
                    perfil = form.save(commit=False)
                    perfil.user = request.user
                except ValueError:
                    messages.warning(request,'Verificar Datos')
                    return render(request, 
                      'cuentas/editarPerfil.html', 
                      {'form':form})
                    
            perfil.save()  
            return redirect('perfil')
        
            