from django.contrib import admin
from .models import Producto, tipoProducto, stockProducto
# Register your models here.

admin.site.register(Producto)
admin.site.register(tipoProducto)
admin.site.register(stockProducto)