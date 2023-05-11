from typing import Any
from django.db import models


# Create your models here.
class Personas(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length = 100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    dni = models.IntegerField( unique=True, verbose_name='DNI')
    cuit = models.BigIntegerField( unique=True, verbose_name='CUIT')
    email = models.EmailField(max_length=150,unique=True, verbose_name='Email')
    alta = models.BooleanField(verbose_name='Activo',default=True)
   
    
    class Meta:
        abstract=True
        

class Empleado(Personas):
    
       
    direccion= models.CharField(max_length=200, verbose_name='Direccion', blank=False)
    telefono = models.CharField(max_length=20, verbose_name='Telefono', blank=False)
    cargo = models.CharField(max_length = 150, verbose_name='Cargo')
    sueldo = models.IntegerField(verbose_name='Sueldo')

      
    def __str__(self):
        return f"{self.nombre} - {self.dni} - {self.alta}"
    
    def darBajar(self):
        if self.alta:
            self.alta = False
            super().save()
        else:
            return f"{self.usuario} ya esta dado de Baja"
    def restaurar(self):
        if self.alta:
            return f"{self.usuario} ya esta dado de Alta"
        else:
            self.alta = True
            super().save()
    
    class Meta:
        db_table = 'empleado'
        managed = True
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Cliente(Personas):
    
    def __str__(self):
        return f"{self.nombre} - {self.dni} - {self.alta}"
    
    def darBajar(self):
        if self.alta:
            self.alta = False
            super().save()
        else:
            return f"{self.usuario} ya esta dado de Baja"
    def restaurar(self):
        if self.alta:
            return f"{self.usuario} ya esta dado de Alta"
        else:
            self.alta = True
            super().save()
            
    class Meta:
        db_table = 'cliente'
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
class Direccion(models.Model):
    alias = models.CharField(max_length=50, unique=False, verbose_name='Alias')
    calle = models.CharField(max_length=100, null=False, verbose_name='Direccion Exacta')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    cp = models.IntegerField( verbose_name='Codigo Postal')
    telefono = models.IntegerField(verbose_name='Telefono')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str(self):
        return self.alias
    
    class Meta:
        db_table = 'direccion_cliente'
        managed = True
        verbose_name = 'Direccion Cliente'
        verbose_name_plural = 'Direcciones Clientes'        
    
    
    

    
    
    
    
 