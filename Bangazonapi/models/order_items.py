from django.db import models
from .order import Order
from .product import Product

class OrderItems(models.Model):
    """Model that represents a rare user"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    