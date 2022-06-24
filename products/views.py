from django.shortcuts import render


def home_page(request):
    age = 22
    name = 'Aleksey'
    return render(request, 'products/home_page.html', locals())
