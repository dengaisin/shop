from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductPhoto(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='product_images')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'