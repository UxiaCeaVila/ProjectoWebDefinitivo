from datetime import timezone

from django.shortcuts import render

from .forms import ProductForm
from .models import Product


# Create your views here.

def frontpage(request):
    return render(request,'frontpage.html')
def information(request):
    return render(request,'information.html')
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
    return render(request,'venderProducto.html',{'form': form})