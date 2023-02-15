from django.db import models


# Create your models here.
class Product(models.Model):
    numserie = models.AutoField(auto_created=True,serialize=False, verbose_name='ID', primary_key= True)
    nombre = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    version = models.CharField(max_length=150)
    precio = models.CharField(max_length=150)
