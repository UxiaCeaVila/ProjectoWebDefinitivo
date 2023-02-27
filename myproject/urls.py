from django.urls import path
from . import views

app_name="gestion"
urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('robots/verproducts', views.listaproducts, name="listarProducts"),
    path('robots/crearproducts', views.ventaproducts, name="nuevoProducts"),
    path('clientes/listarClientes', views.listaclients, name="listarClientes"),
    path('robots/nuevoCliente', views.nuevoclient, name="nuevoCliente"),
    path('cliente/borrar/<idclient>', views.borrarCliente, name="borrarCliente"),
]