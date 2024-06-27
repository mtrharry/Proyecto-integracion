# En views.py
from core.models import Producto, tipoProducto,stockProducto
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_api.serializers import ProductoSerializer, TipoProductoSerializer, stockProductoSerializer
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.shortcuts import render, redirect
from requests import Response
# views.py
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transbank.webpay.webpay_plus.transaction import Transaction

class InitTransactionView(APIView):
    def post(self, request):
        buy_order = request.POST.get('buy_order')
        session_id = request.POST.get('session_id')
        amount = request.POST.get('amount')
        # Utiliza la URL de tu túnel de desarrollo para la URL de retorno
        return_url = 'https://3wxnjnk9-8000.brs.devtunnels.ms/' + reverse('commit_transaction')
        #return_url = 'http://127.0.0.1:8000/commit_transaction'
    
        tx = Transaction()
        response = tx.create(buy_order, session_id, amount, return_url)
        
        if response['token']:
            return redirect(response['url'] + '?token_ws=' + response['token'])
        return Response(response, status=status.HTTP_200_OK)
    
from django.http import QueryDict
def transaction_details(request):
    return render(request, 'core/boleta.html')

def commit_transaction(request):
    token = request.GET.get('token_ws')
    tx = Transaction()
    response = tx.commit(token)

    if response:
        query_params = f"?token_ws={token}&vci={response['vci']}&amount={response['amount']}&status={response['status']}&buy_order={response['buy_order']}&session_id={response['session_id']}&card_number={response['card_detail']['card_number']}&accounting_date={response['accounting_date']}&transaction_date={response['transaction_date']}&authorization_code={response['authorization_code']}&payment_type_code={response['payment_type_code']}&response_code={response['response_code']}&installments_number={response['installments_number']}"
        return redirect(reverse('transaction_details') + query_params)

    return Response(response, status=status.HTTP_200_OK)


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
    
    # Verificar si ya existe un stock asociado al producto
    id_producto = datos_stock.get('idProducto')
    if id_producto is not None:
        try:
            stock_existente = stockProducto.objects.filter(idProducto=id_producto)
            if stock_existente.exists():
                # Si hay registros de stock asociados, devolver un mensaje de error
                return Response({'message': 'Ya existe un stock asociado a este producto. Utiliza un método PUT para actualizar el stock.'}, status=status.HTTP_400_BAD_REQUEST)
        except stockProducto.DoesNotExist:
            pass  # Si no hay un stock existente, continuar con la creación
    
    serializer = stockProductoSerializer(data=datos_stock)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def actualizar_producto(request, id):
    try:
        producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Producto no encontrado'})
    
    if request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # Actualizar el stock si la cantidad de stock se proporciona en la solicitud
            cantidad_nueva = request.data.get('cantidadstock')
            if cantidad_nueva is not None:
                stock_producto = producto.cantidadstock
                if stock_producto:
                    stock_producto.cantidad = cantidad_nueva
                    stock_producto.save()
                else:
                    # Si no hay un stock existente, crear uno nuevo
                    stock_producto = stockProducto.objects.create(idProducto=producto, cantidad=cantidad_nueva)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def actualizar_tipoproducto(request, id):
    try:
        tipoproducto = tipoProducto.objects.get(idTipoProducto=id)
    except tipoProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Tipo de Producto no encontrado'})
    
    if request.method == 'PUT':
        serializer = TipoProductoSerializer(tipoproducto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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
    
@api_view(['delete'])
def eliminar_tipoproducto(request, id):
    try:
        tipoproducto = tipoProducto.objects.get(idTipoProducto=id)
        
    except tipoProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Tipo de Producto no encontrado'})
    
    if request.method == 'DELETE':
        tipoproducto.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Tipo de Producto eliminado'})

@api_view(['delete'])
def eliminar_stock(request, id):
    try:
        stock = stockProducto.objects.get(idStockProducto=id)
        
    except stockProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Stock de Producto no encontrado'})
    
    if request.method == 'DELETE':
        stock.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Stock de Producto eliminado'})
    
def index(request):
    return render(request, 'core/index.html')

def payment_form(request):
    return render(request, 'core/pago.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')

def contactanos(request):
    return render(request, 'core/contactanos.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')
