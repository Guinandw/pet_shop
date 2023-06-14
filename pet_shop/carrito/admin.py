from django.contrib import admin
from .models import Orden,Orden_detalle
# Register your models here.
admin.site.register(Orden)
admin.site.register(Orden_detalle)