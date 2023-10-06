from django.db import models

# Create your models here.

class   Products(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    code = models.CharField(max_length=5)
    price = models.IntegerField()
    status = models.CharField(max_length=20)
    stock = models.IntegerField()
    category = models.CharField(max_length=20)
    # thumbnail = models.ImageField() #No paso el manage.py check. Ver alternativas

class Users(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
    password = models.CharField(max_length=20)
    rol = models.CharField(max_length=20) # en realidad deberia configurar opciones: "admin", "user", "premium"
    #last_connection = models.DateField()

class Carts(models.Model):
    #products = models.CharField(max_length=100) # Desarrollar. Deberia ser un array que tenga el codigo de producto y qty de cada producto agregado al carrito.
    product = models.CharField(max_length=5) # Iria el codigo del producto. 
    qty = models.IntegerField() # Cantidad del producto