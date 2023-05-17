from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil
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







class userFormCompleto(forms.ModelForm):
    
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
        validators=(validador_email,),
        error_messages={ 
                        "required":'Correo Invalido'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo', 'type':'email'})
        )
    
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        max_length=100,
        validators=(validador_nombres,),
        error_messages={'required':'probando'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre...'})
    )
    
    last_name = forms.CharField(
        label='Apellido',
        max_length=100,
        validators=(validador_nombres,),
        error_messages={'required':'probando'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido...'})
    )
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')




class PerfilForm(forms.ModelForm):
    
    
    dni = forms.IntegerField(
        label='DNI',
        min_value=1000000,
        max_value=99999999,
        required=True,
        error_messages={
            'required':'Ha ingresado un DNI invalido'
        },
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'DNI...', 'type':'number'})
    )
    
    cuit = forms.IntegerField(
        label='CUIT',
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
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion...','type':'text'})
    )
    
        
    ciudad = forms.CharField(
        label='Ciudad',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad...','type':'text'})
    ) 
    
    cp = forms.IntegerField(
        label='Codigo Postal',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Codigo Postal...','type':'number'})
    )
    
    telefono = forms.IntegerField(
        label='Telefono',
        required=True,
        error_messages={
            'required':'Ha ingresado un telefono invalido'
        },
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Solo Numeros...', 'type':'number'})
    )
    
    
    def clean_mensaje(self):
        dni = self.cleaned_data['dni']
        if len(dni) < 6 and len(dni)>8:
            raise ValidationError('Debe tener 6 digitos o mas.')
        return dni
    
    class Meta:
        model = Perfil
        fields = ('dni', 'cuit', 'direccion', 'ciudad', 'cp', 'telefono')


class editarUsuario(forms.ModelForm):
    
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        max_length=100,
        validators=(validador_nombres,),
        error_messages={'required':'probando'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre...'})
    )
    
    last_name = forms.CharField(
        label='Apellido',
        max_length=100,
        validators=(validador_nombres,),
        error_messages={'required':'probando'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido...'})
    )
    
    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo'
        }  
        
    
       
    
    