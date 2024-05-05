# En views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, UsuarioSerializer
from rest_framework import generics
from datetime import datetime

@csrf_exempt
@api_view(['GET'])
def lista_producto(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


    
