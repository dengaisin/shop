from django.contrib import admin

from .models import ProductPhoto, Product, Category

admin.site.register(ProductPhoto)
admin.site.register(Product)
admin.site.register(Category)

