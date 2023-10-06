from django.contrib import admin
from .models import products, users, carts

admin.site.register(products)
admin.site.register(users)
admin.site.register(carts)

