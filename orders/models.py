from django.db import models
from customers.models import Profile


class Order(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    customer = models.ForeignKey(to=Profile, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.customer.user.username}"
