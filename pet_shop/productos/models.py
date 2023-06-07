from django.db import models

# Create your models here.
class Animal(models.Model):
    tipo = models.CharField(verbose_name='tipo', max_length=20)
    
    def __str__(self):
        return self.tipo
    
class Raza(models.Model):
    raza = models.CharField(verbose_name='raza',max_length=20)
    tamanio = models.CharField(verbose_name='tamaño',max_length=20)
    tipo = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tipo} {self.tamanio}"
    
class Productor(models.Model):
    marca = models.CharField(verbose_name='marca', max_length=50)
    origen = models.CharField(verbose_name='pais', max_length=50)
    
    def __str__(self):
        return self.marca

class Proveedor(models.Model):
    empresa = models.CharField(verbose_name='nombre empresa', max_length=100)
    contacto = models.CharField(verbose_name='contacto', max_length=50)
    cargo_contacto = models.CharField(verbose_name='cargo contacto', max_length=100)
    telefono = models.CharField(verbose_name='Telefono', max_length=50, blank=True)
    cuit = models.CharField(verbose_name='CUIT', max_length=11)
    
    def __str__(self):
        return self.empresa
    
class Producto(models.Model):
    codigo = models.CharField(verbose_name='codigo', max_length=3)
    nombre = models.CharField(verbose_name='nombre', max_length=50)
    tipo = models.CharField(verbose_name='tipo', max_length=50, blank=True)
    descripcion = models.TextField(verbose_name='descripcion')
    formato = models.CharField(verbose_name='formato', max_length=100, blank=True)
    precio = models.IntegerField(verbose_name='precio')
    enStock = models.BooleanField(verbose_name='estado')
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name='Imagen', blank=True, upload_to='producto/')
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.codigo}"
    
    