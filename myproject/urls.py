from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('robots/information', views.information, name="information"),
    path('robots/products', views.products, name="products"),
    path('login', views.login, name="login"),
    path('register', views.registro, name="registro"),
]