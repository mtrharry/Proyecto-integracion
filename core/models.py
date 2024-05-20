from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='Id de Producto')
    idTipoProducto = models.ForeignKey('tipoProducto', on_delete=models.PROTECT, verbose_name='Id de Tipo de Producto')
    cantidadstock = models.ForeignKey('stockProducto', on_delete=models.CASCADE , verbose_name='Cantidad en Stock', null=True,blank=True)

    def __str__(self):
        return str(self.idTipoProducto.descripcionTipoProducto)
    
    
class tipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True, verbose_name='Id de Tipo de Producto')
    nombreTipoProducto = models.CharField(max_length=50, verbose_name='Nombre de Tipo de Producto')
    descripcionTipoProducto = models.CharField(max_length=50, verbose_name='Descripcion de Tipo de Producto')
    
    def __str__(self):
        return self.nombreTipoProducto
    
class stockProducto(models.Model):
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name='Id de Producto')                        
    cantidad = models.IntegerField(verbose_name='Stock de Producto', null=True) 
    
    def __str__(self):
        return str(self.cantidad)

@receiver(post_save, sender=stockProducto)
def actualizar_stock_producto(sender, instance, **kwargs):
    producto = instance.idProducto
    producto.cantidadstock = instance
    producto.save()

