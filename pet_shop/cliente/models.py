from django.db import models
from productos.models import Producto
from cuentas.models import User
# Create your models here.


class Favoritos(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    

    
    


