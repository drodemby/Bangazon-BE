from django.db import models
from .seller import Seller
from .category import Category

class Product(models.Model):
    """Model that represents a rare user"""
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=10000)
    description = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    isAvailble = models.BooleanField()
    