from django.urls import path
from rest_api.views import lista_producto, crear_producto, eliminar_producto,actualizar_producto

urlpatterns = [
    path('productos/', lista_producto),
    path('post/productos/', crear_producto),
    path('delete/productos/<int:id>/', eliminar_producto),
    path('put/productos/<int:id>/', actualizar_producto),
]