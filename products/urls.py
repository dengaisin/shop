from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='home-page'),
    # path('<int:id>', views.product_detail, nmae='product-detail'),
]
