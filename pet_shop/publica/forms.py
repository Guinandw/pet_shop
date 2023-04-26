from django import forms
from django.forms import ValidationError



class ContactanosForms(forms.Form):
    
    nombre = forms.CharField(label='Nombre',
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
