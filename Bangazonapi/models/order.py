from django.db import models
from .customer import Customer
from .seller import Seller

class OrderItems(models.Model):
    """Model that represents a rare user"""
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    status = models.BooleanField()
    