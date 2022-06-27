from django.contrib import admin

from .models import ProductPhoto, Product, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProductPhoto)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

