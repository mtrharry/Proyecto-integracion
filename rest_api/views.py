# En views.py
from core.models import Producto
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_api.serializers import ProductoSerializer
from rest_framework import status
from rest_framework.exceptions import ParseError

@api_view(['GET'])
def lista_producto(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def crear_producto(request):
    datos_producto = request.data
    
    serializers = ProductoSerializer(data=datos_producto)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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