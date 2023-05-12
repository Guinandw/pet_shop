from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import userFormCompleto 
from django.contrib.auth.models import User
from django.db import IntegrityError

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
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'crearCuenta.html', {'form':userFormCompleto} )
          
def logout(request):
    logout(request)
    return render(request, 'inicio')
    