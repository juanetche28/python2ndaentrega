from django import forms

class ProductForm(forms.Form):
    #Especifico los campos
    title = forms.CharField(max_length=20)
    description = forms.CharField(max_length=40)
    code = forms.CharField(max_length=5)
    price = forms.IntegerField()
    status = forms.CharField(max_length=20)
    stock = forms.IntegerField()
    category = forms.CharField(max_length=20)

class UserForm(forms.Form):
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    age = forms.IntegerField()
    password = forms.CharField(max_length=20)
    rol = forms.CharField(max_length=20)

class CartForm(forms.Form):
    product = forms.CharField(max_length=5)
    qty = forms.IntegerField()

class BuscaProductForm(forms.Form):
    product = forms.CharField()