from django.urls import path
from rest_api.views import lista_producto,obtener_producto, lista_stock,obtener_tipoproducto,obtener_stock
from rest_api.views import crear_producto,crear_tipoproducto,crear_stock
from rest_api.views import eliminar_producto
from rest_api.views import actualizar_producto

urlpatterns = [
    path('productos/', lista_producto),
    path('productos/<int:id>/', obtener_producto),
    path('tipoproducto/<int:id>/', obtener_tipoproducto),
    path('listastock/', lista_stock),
    path('listastock/<int:id>/', obtener_stock),

    path('post/creartipo', crear_tipoproducto),
    path('post/productos/', crear_producto),
    path('post/stock/', crear_stock),

    path('delete/productos/<int:id>/', eliminar_producto),
    path('put/productos/<int:id>/', actualizar_producto),
]