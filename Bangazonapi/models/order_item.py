from django.db import models
from .order import Order
from .product import Product

class OrderItem(models.Model):
    """Model that represents a rare user"""
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    