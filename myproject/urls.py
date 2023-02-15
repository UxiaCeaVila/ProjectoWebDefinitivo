from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('robots/information', views.information, name="information"),
    path('robots/verproducts', views.listaproducts, name="listarProducts"),
    path('robots/crearproducts', views.ventaproducts, name="venderProducts"),

]