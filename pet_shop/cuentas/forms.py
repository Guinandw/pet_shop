from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

def validador_nombres(value):
    print('VALIDADOR NOMBRE')
    for i in value:
        if (i.isdigit()):
            raise ValidationError(f'{value} no es un nombre valido', code='Invalid', params={'valor':value})
    
        
def validador_numeros(value):
    print('VALIDADOR NUMERO')
    for i in value:
        if (i.isdigit()):
            pass
        else: raise ValidationError(f'No ingrese ni letras ni signos.', code='Invalid', params={'valor':value})
        
def validador_email(value):
    print('VALIDADOR EMAIL')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value



class userFormCompleto(UserCreationForm):
    
    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Alias...'})
    )
    
    password1 = forms.CharField(
        label='Password',
        required=True,
        max_length=100,
        min_length=8,
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    
    password2 = forms.CharField(
        label='Confirmar Password',
        required=True,
        max_length=100,
        min_length=8,
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    
    email = forms.EmailField(
        max_length=200, 
        label='Correo',
        error_messages={ 
                        "required":'Correo Invalido'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo', 'type':'email'})
        )
    
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        max_length=100,
        validators=(validador_nombres,),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre...'})
    )
    
    last_name = forms.CharField(
        label='Apellido',
        max_length=100,
        validators=(validador_nombres,),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido...'})
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')




class PerfilForm(forms.Form):
    
    
    dni = forms.CharField(
        label='DNI',
        max_length=11,
        validators=(validador_numeros,),
        required=True,
        error_messages={
            'required':'Ha ingresado un DNI invalido'
        },
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'DNI...', 'type':'number'})
    )
    
    cuit = forms.CharField(
        label='CUIT',
        max_length=11,
        validators=(validador_numeros,),
        required=True,
        error_messages={
            'required':'Ha ingresado un CUIT invalido'
        },
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CUIT...', 'type':'number'})
    )
    
    direccion = forms.CharField(
        label='Direccion de Envio',
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion...'})
    )
    
        
    ciudad = forms.CharField(
        label='Ciudad',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad...'})
    ) 
    
    cp = forms.CharField(
        label='Codigo Postal',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'direccion...'})
    )
    
    telefono = forms.CharField(
        label='Telefono',
        max_length=15,
        required=True,
        validators=(validador_numeros, ),
        error_messages={
            'required':'Ha ingresado un telefono invalido'
        },
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Solo Numeros...', 'type':'number'})
    )
    
    
    def clean_mensaje(self):
        usuario = self.cleaned_data['usuario']
        if len(usuario) < 6:
            raise ValidationError('Debe tener 6 digitos o mas.')
        return usuario
    
    

    
       
    
    