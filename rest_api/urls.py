# En urls.py

from django.urls import path
from rest_api.views import (
    lista_producto, obtener_producto, lista_stock, obtener_tipoproducto, obtener_stock, lista_tipo,
    crear_stock, crear_producto, crear_tipoproducto, actualizar_producto, eliminar_producto,
    eliminar_tipoproducto, eliminar_stock, actualizar_tipoproducto, transaction_details
)
from .views import payment_form, InitTransactionView, commit_transaction, index, catalogo, contactanos, nosotros

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

    path('payment_form/', payment_form, name='payment_form'),
    path('init_transaction/', InitTransactionView.as_view(), name='init_transaction'),
    path('commit_transaction/', commit_transaction, name='commit_transaction'),
    path('transaction_details/', transaction_details, name='transaction_details'),

    path('', index, name='index'),
    path('catalogo/', catalogo, name='catalogo'),
    path('contactanos/', contactanos, name='contactanos'),
    path('nosotros/', nosotros, name='nosotros'),

    
]
