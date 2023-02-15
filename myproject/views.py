from datetime import timezone

from django.shortcuts import render
# Create your views here.

def frontpage(request):
    return render(request,'frontpage.html')
def information(request):
    return render(request,'information.html')
def products(request):
    return render(request,'listarProducts.html')