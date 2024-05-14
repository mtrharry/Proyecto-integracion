# En views.py
from core.models import Producto, tipoProducto,stockProducto
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_api.serializers import ProductoSerializer, TipoProductoSerializer, stockProductoSerializer
from rest_framework import status
from rest_framework.exceptions import ParseError


@api_view(['GET'])
def lista_producto(request):
    if request.method == 'GET':
        productos = Producto.objects.all().order_by('idProducto')
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def obtener_producto(request, id):
    try:
        producto = Producto.objects.get(idProducto=id)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Producto no encontrado'})

@api_view(['GET'])
def lista_tipo(request):
    if request.method == 'GET':
        tipo = tipoProducto.objects.all().order_by('idTipoProducto')
        serializer = TipoProductoSerializer(tipo, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def obtener_tipoproducto(request, id):
    try:
        tipoproducto = tipoProducto.objects.get(idTipoProducto=id)
        serializer = TipoProductoSerializer(tipoproducto)
        return Response(serializer.data)
    except tipoProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Tipo de Producto no encontrado'})
    
@api_view(['GET'])
def lista_stock(request):
    if request.method == 'GET':
        stock = stockProducto.objects.all()
        serializer = stockProductoSerializer(stock, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def obtener_stock(request, id):
    try:
        stock = stockProducto.objects.get(idStockProducto=id)
        serializer = stockProductoSerializer(stock)
        return Response(serializer.data)
    except stockProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Stock de Producto no encontrado'})

@api_view(['POST'])
def crear_tipoproducto(request):
    datos_tipoproducto = request.data
    
    serializers = TipoProductoSerializer(data=datos_tipoproducto)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

    
@api_view(['POST'])
def crear_producto(request):
    datos_producto = request.data
    
    serializer = ProductoSerializer(data=datos_producto)  # Corregido el nombre de la variable a 'serializer'

    if serializer.is_valid():  # Corregido el nombre de la variable a 'serializer'
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_stock(request):
    datos_stock = request.data
    
    serializer = stockProductoSerializer(data=datos_stock)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['delete'])
def eliminar_producto(request, id):
    try:
        producto = Producto.objects.get(idProducto=id)
        
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Producto no encontrado'})
    
    if request.method == 'DELETE':
        producto.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Producto eliminado'})
    
@api_view(['PUT'])
def actualizar_producto(request, id):
    try:
        producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Producto no encontrado'})
    
    if request.method == 'PUT':
        serializers = ProductoSerializer(producto, data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)