from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre de Producto')
    precioProducto = models.IntegerField(verbose_name='Precio de Producto')
    idTipoProducto = models.ForeignKey('tipoProducto', on_delete=models.PROTECT, verbose_name='Id de Tipo de Producto')
    
    

    def __str__(self):
        return self.nombreProducto
    
    
class tipoProducto(models.Model):
    idTipoProducto = models.IntegerField(primary_key=True, verbose_name='Id de Tipo de Producto')
    nombreTipoProducto = models.CharField(max_length=50, verbose_name='Nombre de Tipo de Producto')
    descripcionTipoProducto = models.CharField(max_length=50, verbose_name='Descripcion de Tipo de Producto')
    
    def __str__(self):
        return self.nombreTipoProducto
    
class stockProducto(models.Model):
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name='Id de Producto')
    stockProducto = models.IntegerField(verbose_name='Stock de Producto')
    
    def __str__(self):
        return self.stockProducto
