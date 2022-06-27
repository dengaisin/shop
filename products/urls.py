from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('<slug:slug>', views.product_detail, name='product-detail'),

]
