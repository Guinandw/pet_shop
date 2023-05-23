from django.forms import forms, ModelForm
from django import forms
from .models import Blog

class BlogCrearForm(ModelForm):
    
    
    class Meta:
        model = Blog
        fields = '__all__'
        widget = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}),
            'contenido': forms.Textarea(attrs={'row':50, 'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'})
        }