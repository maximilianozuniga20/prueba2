from django.urls import path
from .views import home
from .views import principal
from .views import proximo
from .views import stock
from .views import listar
from .views import eliminar

urlpatterns = [
    path('registro/', home, name="juego"),
    path('principal/', principal, name="principal"),
    path('proximo/', proximo, name="proximo"),
    path('stock/', stock, name="stock"),
    path('listar/', listar, name="listar"),
    path('eliminar/', eliminar, name="eliminar"),
]