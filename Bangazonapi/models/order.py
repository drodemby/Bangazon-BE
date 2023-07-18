from django.db import models
from .user import User

class Order(models.Model):
    """Model that represents a rare user"""
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    