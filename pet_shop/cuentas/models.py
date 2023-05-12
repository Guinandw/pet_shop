from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    dni = models.IntegerField( unique=True, verbose_name='DNI')
    cuit = models.BigIntegerField( unique=True, verbose_name='CUIT')
    direccion = models.CharField(max_length=100, null=False, verbose_name='Direccion Exacta')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    cp = models.IntegerField( verbose_name='Codigo Postal')
    telefono = models.IntegerField(verbose_name='Telefono')
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
            
    class Meta:
        db_table = 'perfil'
        managed = True
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
