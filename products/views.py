from django.shortcuts import render
from .models import ProductPhoto


def home_page(request):
    prod_photos = ProductPhoto.objects.filter(is_active=True, is_main=True)
    return render(request, 'products/home_page.html', locals())


def product_detail(request, id):
    prod_photo = ProductPhoto.objects.get(id=id)
    return render(request, 'products/product-detail.html', locals())
