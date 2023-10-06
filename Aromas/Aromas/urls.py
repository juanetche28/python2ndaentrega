from django.contrib import admin
from django.urls import path
from AppAromas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('productsForm/', views.productsForm, name="productsForm"),
    path('cartsForm/', views.cartsForm, name="cartsForm"),
    path('usersForm/', views.usersForm, name="usersForm"),
    path('products/', views.products, name="products"),
    path('users/', views.users, name="users"),
    path('carts/', views.carts, name="carts"),
    path('search/', views.search, name="search"),
    path('show-products/', views.show_products, name="Show_Products"),

]