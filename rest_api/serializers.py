from rest_framework import serializers
from core.models import Usuario, Categoria, Producto
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria', 'nombreCategoria']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'stockProducto', 'categoria_id']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'nombreUsuario', 'apellidoUsuario', 'emailUsuario', 'passwordUsuario', 'telefonoUsuario']
