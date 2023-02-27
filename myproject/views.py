from datetime import timezone

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .forms import ClientForm, VentaForm
from .models import Product
from .models import Client,Venta


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
def borrarProducto(request, numserie):
   product = get_object_or_404(Product, numserie=numserie)
   product.delete()
   return redirect('gestion:listarProducts')
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
def listaventas(request,idclient):
    ventas = Venta.objects.filter(idclient=idclient).order_by("idventa")
    return render(request,'listarVentas.html', {'clients': ventas})
def nuevaventa(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            print("vamos bien")
            venta = form.save()
            venta.save()
    else:
        print("no vamos bien")
        form = VentaForm()
    return render(request,'nuevaVenta.html',{'form': form})
def borrarventa(request, idclient, idventa):
   venta = get_object_or_404(Client, idventa=idventa)
   venta.delete()
   return redirect('gestion:listarVentas')