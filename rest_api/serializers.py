from rest_framework import serializers
from core.models import Producto, tipoProducto, stockProducto

class TipoProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = tipoProducto
        fields = 'idTipoProducto','nombreTipoProducto', 'descripcionTipoProducto'



class ProductoSerializer(serializers.ModelSerializer):
    nombreTipoProducto = serializers.CharField(source='idTipoProducto.nombreTipoProducto', read_only=True)
    descripcionTipoProducto = serializers.CharField(source='idTipoProducto.descripcionTipoProducto', read_only=True)
    class Meta:
        model = Producto
        fields = 'idProducto','idTipoProducto','nombreTipoProducto','descripcionTipoProducto','stockProducto'
    
class stockProductoSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = stockProducto
            fields = 'idStockProducto','idProducto','stockProducto'
