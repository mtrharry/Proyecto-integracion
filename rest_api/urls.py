from django.urls import path
from rest_api.views import lista_producto

urlpatterns = [
    path('productos/', lista_producto),
]