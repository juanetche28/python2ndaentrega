from django.contrib import admin
from django.urls import path
from AppAromas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productsForm/', views.productsForm, name="productsForm"),
    path('cartsForm/', views.cartsForm, name="cartsForm"),
    path('usersForm/', views.usersForm, name="usersForm"),
    path('products/', views.products, name="products"),
    path('users/', views.users, name="users"),
    path('carts/', views.carts, name="carts"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
    path('mostrar-products/', views.mostrar_products, name="Mostrar_Products"),
]