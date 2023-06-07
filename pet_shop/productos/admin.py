from django.contrib import admin
from .models import Animal, Raza, Productor, Proveedor, Producto

# Register your models here.
admin.site.register(Animal)
admin.site.register(Raza)
admin.site.register(Productor)
admin.site.register(Proveedor)
admin.site.register(Producto)