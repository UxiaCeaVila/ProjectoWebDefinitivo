from django import forms
from .models import Product
from .models import Client

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['numserie', 'nombre', 'modelo', 'version', 'precio']
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['idclient', 'nombre', 'dniclient', 'fecnac']