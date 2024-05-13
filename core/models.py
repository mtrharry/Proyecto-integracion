from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='Id de Producto')
    idTipoProducto = models.ForeignKey('tipoProducto', on_delete=models.PROTECT, verbose_name='Id de Tipo de Producto')
    stockProducto = models.ForeignKey('stockProducto', on_delete=models.PROTECT, verbose_name='Stock de Producto')
    

    def __str__(self):
        return self.idProducto
    
    
class tipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True, verbose_name='Id de Tipo de Producto')
    nombreTipoProducto = models.CharField(max_length=50, verbose_name='Nombre de Tipo de Producto')
    descripcionTipoProducto = models.CharField(max_length=50, verbose_name='Descripcion de Tipo de Producto')
    
    def __str__(self):
        return self.nombreTipoProducto
    
class stockProducto(models.Model):
    idStockProducto = models.AutoField(primary_key=True, verbose_name='Id de Stock de Producto')
    idProducto = models.ForeignKey('Producto', on_delete=models.PROTECT, verbose_name='Id de Producto')                        
    stockProducto = models.IntegerField(verbose_name='Stock de Producto')
    
    def __str__(self):
        return self.stockProducto
