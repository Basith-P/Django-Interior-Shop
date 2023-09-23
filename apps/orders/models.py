from django.db import models

from apps.products.models import Product
from apps.vendor.models import Vendor


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    Vendors = models.ManyToManyField(Vendor, related_name="orders")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.pk}: {self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    vendor = models.ForeignKey(
        Vendor, related_name="order_items", on_delete=models.CASCADE
    )
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}: {self.quantity}"
