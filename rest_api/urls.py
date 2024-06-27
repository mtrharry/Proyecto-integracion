from django.urls import path
from .views import (
    InitTransactionView, transaction_details, commit_transaction,
    index, payment_form, catalogo, contactanos, nosotros,
    lista_producto, obtener_producto, lista_tipo, obtener_tipoproducto,
    lista_stock, obtener_stock, crear_tipoproducto, crear_producto, crear_stock,
    actualizar_producto, actualizar_tipoproducto, eliminar_producto, eliminar_tipoproducto, eliminar_stock
)

urlpatterns = [
    path('', index, name='index'),
    path('payment_form/', payment_form, name='payment_form'),
    path('init_transaction/', InitTransactionView.as_view(), name='init_transaction'),
    path('commit_transaction/', commit_transaction, name='commit_transaction'),
    path('transaction_details/', transaction_details, name='transaction_details'),
    path('catalogo/', catalogo, name='catalogo'),
    path('contactanos/', contactanos, name='contactanos'),
    path('nosotros/', nosotros, name='nosotros'),
    path('productos/', lista_producto, name='lista_producto'),
    path('productos/<int:id>/', obtener_producto, name='obtener_producto'),
    path('tipoproducto/', lista_tipo, name='lista_tipo'),
    path('tipoproducto/<int:id>/', obtener_tipoproducto, name='obtener_tipoproducto'),
    path('listastock/', lista_stock, name='lista_stock'),
    path('listastock/<int:id>/', obtener_stock, name='obtener_stock'),
    path('post/creartipo/', crear_tipoproducto, name='crear_tipoproducto'),
    path('post/productos/', crear_producto, name='crear_producto'),
    path('post/stock/', crear_stock, name='crear_stock'),
    path('put/productos/<int:id>/', actualizar_producto, name='actualizar_producto'),
    path('put/tipoproducto/<int:id>/', actualizar_tipoproducto, name='actualizar_tipoproducto'),
    path('delete/productos/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('delete/tipoproducto/<int:id>/', eliminar_tipoproducto, name='eliminar_tipoproducto'),
    path('delete/stock/<int:id>/', eliminar_stock, name='eliminar_stock'),
]
