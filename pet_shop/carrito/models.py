from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User
# Create your models here.
class Orden(models.Model):
    no_factura = models.IntegerField(unique=True, verbose_name='Numero Factura', blank=True, null=True )
    fecha = models.DateTimeField(verbose_name='Fecha', auto_now_add=True )
    total = models.IntegerField(verbose_name='total', blank=True, null=True)
    estado = models.CharField(verbose_name='estado', max_length=50, default='verificando')
    direccion = models.CharField(verbose_name='direccion', max_length=200)
    ciudad = models.CharField(verbose_name='ciudad', max_length=50)
    cp = models.IntegerField(verbose_name='Codigo Postal')
    telefono = models.CharField(verbose_name='Telefono', max_length=20)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through="Orden_detalle")
    nombre = models.CharField(verbose_name='nombre', max_length=100, null=True, blank=True)
    apellido = models.CharField(verbose_name='apellido', max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        if self.no_factura:
            return f" {self.no_factura} {self.cliente.first_name} {self.fecha.strftime('%d/%m/%y /%H:%M')} "
        return f" Pendiente {self.cliente.first_name} {self.fecha.strftime('%d/%m/%y /%H:%M')} "
    
   
            
    
class Orden_detalle(models.Model):
    precio_unitario = models.IntegerField(verbose_name='precio unitario', blank=True, null=True)
    cantidad = models.IntegerField(verbose_name='cantidad')
    descuento = models.IntegerField(verbose_name='descuento', blank=True, null=True, default=0)
    subtotal = models.FloatField(verbose_name='subtotal', blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.orden.pk} {self.producto.nombre} "
        