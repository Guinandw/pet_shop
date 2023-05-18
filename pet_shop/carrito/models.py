from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User
# Create your models here.
class Orden(models.Model):
    no_factura = models.IntegerField(unique=True, verbose_name='Numero Factura')
    fecha = models.DateTimeField(verbose_name='Fecha', auto_now_add=True )
    total = models.IntegerField(verbose_name='total', blank=True, null=True)
    estado = models.CharField(verbose_name='estado', max_length=50, default='verificando')
    direccion = models.CharField(verbose_name='direccion', max_length=200)
    ciudad = models.CharField(verbose_name='ciudad', max_length=50)
    cp = models.IntegerField(verbose_name='Codigo Postal')
    telefono = models.CharField(verbose_name='Telefono', max_length=20)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Orden_detalle(models.Model):
    precio_unitario = models.IntegerField(verbose_name='precio unitario', blank=True, null=True)
    cantidad = models.IntegerField(verbose_name='cantidad')
    descuento = models.IntegerField(verbose_name='descuento', blank=True, null=True, default=0)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


        
        