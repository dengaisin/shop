from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    count = models.IntegerField(blank=False, null=False)


class ProductPhoto(models.Model):
    image = models.ImageField(upload_to='img')
