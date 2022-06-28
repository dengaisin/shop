from django.shortcuts import render, get_object_or_404
from .models import ProductPhoto, Product
from cart.forms import CartAddProductForm


def home_page(request):
    prod_photos = ProductPhoto.objects.filter(is_active=True, is_main=True)
    return render(request, 'products/home_page.html', locals())


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    prod_photo = get_object_or_404(ProductPhoto, product=product.id)

    cart_product_form = CartAddProductForm()
    print(product.title)
    return render(request, 'products/product-detail.html', locals())




