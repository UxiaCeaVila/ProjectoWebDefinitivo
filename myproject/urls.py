from django.urls import path
from . import views

app_name="gestion"
urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('robots/verproducts', views.listaproducts, name="listarProducts"),
    path('robots/crearproducts', views.ventaproducts, name="nuevoProducts"),
    path('robots/borrar/<numserie>', views.borrarProducto, name="borrarProducts"),
    path('clientes/listarClientes', views.listaclients, name="listarClientes"),
    path('robots/nuevoCliente', views.nuevoclient, name="nuevoCliente"),
    path('cliente/borrar/<idclient>', views.borrarCliente, name="borrarCliente"),
    path('ventas/<idclient>/listarventas', views.listaventas, name="listarVentas"),
    path('ventas/nuevaventa>', views.nuevaventa, name="nuevaVenta"),
    path('ventas/<idclient>/devolver/<idventa>', views.borrarventa, name="devolverVenta"),
]