from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre de Producto')
    precioProducto = models.IntegerField(verbose_name='Precio de Producto')
    stockProducto = models.IntegerField(verbose_name='Stock de Producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto
    
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Id de Usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
    apellidoUsuario = models.CharField(max_length=50, verbose_name='Apellido de Usuario')
    emailUsuario = models.CharField(max_length=50, verbose_name='Email de Usuario')
    passwordUsuario = models.CharField(max_length=50, verbose_name='Password de Usuario')
    telefonoUsuario = models.CharField(max_length=50, verbose_name='Telefono de Usuario')

    def __str__(self):
        return self.nombreUsuario
    
