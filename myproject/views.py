from datetime import timezone

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .forms import ClientForm
from .models import Product
from .models import Client


# Create your views here.

def frontpage(request):
    return render(request,'frontpage.html')
def listaproducts(request):
    products = Product.objects.order_by("numserie")
    return render(request,'listarProducts.html', {'products': products})
def ventaproducts(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            product = form.save()
            product.save()
    else:
        print("no vamos bien")
        form = ProductForm()
    return render(request,'nuevoProducto.html',{'form': form})
def listaclients(request):
    clients = Client.objects.order_by("idclient")
    return render(request,'listarClientes.html', {'clients': clients})
def nuevoclient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            client = form.save()
            client.save()
    else:
        print("no vamos bien")
        form = ClientForm()
    return render(request,'nuevoProducto.html',{'form': form})
def borrarCliente(request, idclient):
   client = get_object_or_404(Client, idclient=idclient)
   client.delete()
   return redirect('gestion:listarClientes')