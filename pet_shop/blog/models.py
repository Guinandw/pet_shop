from django.db import models
from cuentas.models import User
# Create your models here.

class blog(models.Model):
    titulo = models.CharField(max_length=300, null=False,verbose_name='Titulo')
    subtitulo: models.CharField(max_length=300, null=False,verbose_name='Subtitulo')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    contenido = models.TextField(verbose_name='Contenido', )
    imagen = models.ImageField(upload_to='blog/images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
