from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppAromas.models import  Products, Users, Carts
from AppAromas.forms import ProductForm, CartForm, UserForm, BuscaProductForm

# Create your views here.
def home(request):
    return render(request, "AppAromas/index.html")

def productsForm(request):
    if request.method =='POST':

        miFormulario = ProductForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            product = Products (title=informacion['title'],description=informacion['description'],code=informacion['code'],price=informacion['price'],status=informacion['status'],stock=informacion['stock'],category=informacion['category'])
            product.save()
            return render(request, "AppAromas/index.html")
    else:
        miFormulario = ProductForm()

    return render(request, "AppAromas/productsForm.html", {"miFormulario": miFormulario})

def cartsForm(request):
    if request.method =='POST':

        miFormulario = CartForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cart = Carts(product=informacion['product'],qty=informacion['qty'])
            cart.save()
            return render(request, "AppAromas/index.html")
    else:
        miFormulario = CartForm()

    return render(request, "AppAromas/cartsForm.html", {"miFormulario": miFormulario})

def usersForm(request):
    if request.method =='POST':

        miFormulario = UserForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            user = Users(firstName=informacion['firstName'],lastName=informacion['lastName'],email=informacion['email'],age=informacion['age'],password=informacion['password'],rol=informacion['rol'])
            user.save()
            return render(request, "AppAromas/index.html")
    else:
        miFormulario = UserForm()

    return render(request, "AppAromas/usersForm.html", {"miFormulario": miFormulario})
       

def search(request):
    if request.method == "POST":
        miFormulario = BuscaProductForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            products = Products.objects.filter(category__icontains=informacion["product"])

            return render(request, "AppAromas/search_results.html", {"products": products})
    else:
        miFormulario = BuscaProductForm()

    return render(request, "AppAromas/search.html", {"miFormulario": miFormulario})

def show_products(request):

    products = Products.objects.all() #trae todos los productos

    contexto= {"products":products} 

    return render(request, "AppAromas/show_products.html",contexto)






def products(request):
    return render(request, "AppAromas/products.html")

def users(request):
    return render(request, "AppAromas/users.html")

def carts(request):
    return render(request, "AppAromas/carts.html")


