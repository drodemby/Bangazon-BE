from django.db import models

class Customer(models.Model):
    """Model that represents a rare user"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
   
    