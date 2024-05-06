from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre de Producto')
    precioProducto = models.IntegerField(verbose_name='Precio de Producto')
    stockProducto = models.IntegerField(verbose_name='Stock de Producto')
    

    def __str__(self):
        return self.nombreProducto
    
    

