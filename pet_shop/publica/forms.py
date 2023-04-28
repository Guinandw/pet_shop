from django import forms
from django.forms import ValidationError
import re

def validador_nombres(value):
    for i in value:
        if i.isdigit():
            raise ValidationError(f'{value} no es un nombre valido', code='Invalid')
    
        
def validador_numeros(value):
    
        if value.isdecimal():
            return
        else: raise ValidationError(f'No ingrese ni letras ni signos.', code='Invalid')
        
def validador_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value

class ContactanosForms(forms.Form):
    
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Nombre...', 
                })
        )
    
    email = forms.EmailField(
        label='Email',
        max_length=100,
        error_messages={
            'required': 'Por favor ingresar email'
        },
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'type':'email', 
                'placeholder':'Email...'})
    )
    
    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        error_messages={
            'required': 'Asunto sin completar'
        },
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Asunto',
                'type':'text'
            }
        )
    )
    
    mensaje= forms.CharField(
        label='Mensaje',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'rows':5,
            
        })
    )


class EnviosForms(forms.Form):
    
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(validador_nombres,),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre...'})
    )
    
    apellido = forms.CharField(
        label='Apellido',
        max_length=11,
        validators=(validador_nombres,),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido...'})
    )
    
    """ dni = forms.CharField(
        label='DNI',
        max_length=11,
        validators=(validador_numeros,),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CUIT...'})
    )
    
    cuit = forms.CharField(
        label='CUIT',
        max_length=11,
        validators=(validador_numeros,),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CUIT...'})
    ) """
    
    
    direccion = forms.CharField(
        label='Direccion de Envio',
        max_length=200,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion...'})
    )
    
        
    ciudad = forms.CharField(
        label='Ciudad',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad...'})
    ) 
    
    cp = forms.CharField(
        label='Codigo Postal',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'direccion...'})
    )
    
    telefono = forms.IntegerField(
        label='Telefono',
        validators=(validador_numeros, ),
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Solo Numeros...'})
    )
    
    email = forms.EmailField(
        label='Correo Electronico',
        max_length=100,
        validators=(validador_email,),
        error_messages={
            'required': 'Se debe completar el Corrreo Electronico.'
        },
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email', 'type': 'email'})
    )