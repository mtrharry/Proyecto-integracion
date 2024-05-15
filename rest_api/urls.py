from django.urls import path
from rest_api.views import lista_producto,obtener_producto, lista_stock,obtener_tipoproducto,obtener_stock,lista_tipo,crear_stock
from rest_api.views import crear_producto,crear_tipoproducto,actualizar_producto
from rest_api.views import eliminar_producto, eliminar_tipoproducto, eliminar_stock
from rest_api.views import actualizar_producto,actualizar_tipoproducto

urlpatterns = [
    path('productos/', lista_producto),
    path('productos/<int:id>/', obtener_producto),
    path('tipoproducto/<int:id>/', obtener_tipoproducto),
    path('tipoproducto/', lista_tipo),
    path('listastock/', lista_stock),
    path('listastock/<int:id>/', obtener_stock),

    path('post/creartipo/', crear_tipoproducto),
    path('post/productos/', crear_producto),
    path('post/stock/', crear_stock),

    path('put/productos/<int:id>/', actualizar_producto),
    path('put/tipoproducto/<int:id>/', actualizar_tipoproducto),


    path('delete/productos/<int:id>/', eliminar_producto),
    path('delete/tipoproducto/<int:id>/', eliminar_tipoproducto),
    path('delete/stock/<int:id>/', eliminar_stock),    
    
]