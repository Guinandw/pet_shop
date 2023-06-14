from django import forms
from django.forms import ValidationError
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

#se usa en la pagina de CONTACTANOS.
class ContactanosForms(forms.Form):
    
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(validador_nombres,),
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Nombre...', 
                })
        )
    
    email = forms.EmailField(
        label='Email',
        max_length=100,
        validators=(validador_email,),
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
    #solo se va a revisar que el mensaje no este vacio, minimo de 8
    def clean_mensaje(self):
        if (len(self.cleaned_data['mensaje']) < 8):
            raise ValidationError("Favor redactar bien la peticion. Mensaje muy corto.")
        return self.cleaned_data['mensaje']

