from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductPhoto(models.Model):
    image = models.ImageField(upload_to='img')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Product(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    count = models.IntegerField(blank=False, null=False)
    images = models.ForeignKey(to=ProductPhoto, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    """test"""
