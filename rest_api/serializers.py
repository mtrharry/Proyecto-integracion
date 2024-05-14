from rest_framework import serializers
from core.models import Producto, tipoProducto, stockProducto

class TipoProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = tipoProducto
        fields = 'idTipoProducto','nombreTipoProducto', 'descripcionTipoProducto'

class stockProductoSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = stockProducto
            fields = 'idProducto','cantidad'

class ProductoSerializer(serializers.ModelSerializer):
    nombreTipoProducto = serializers.CharField(source='idTipoProducto.nombreTipoProducto', read_only=True)
    descripcionTipoProducto = serializers.CharField(source='idTipoProducto.descripcionTipoProducto', read_only=True)
    cantidadadstock = serializers.CharField(source='cantidadadstock.cantidad', read_only=True)
    class Meta:
        model = Producto
        fields = ('idProducto', 'idTipoProducto', 'nombreTipoProducto', 'descripcionTipoProducto', 'cantidadadstock')