from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class CompletedTransactions(models.Model):
    # Location
    address = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    transaction = models.CharField(max_length=20, choices=[('Leased', 'Leased'), ('Sold', 'Sold')])
    property_type = models.CharField(max_length=30, default="Owner/User")
    category = models.CharField(default='a', max_length=40, choices=[
        ('a', 'Venice'), 
        ('b', 'Sepulveda'), 
        ('c', 'Washington'), 
        ('d', 'LaCienega'), 
        ('e', 'Overland'), 
        ('f', 'Robertson'), 
        ('g', 'Jefferson'),
        ('h', 'W. Adams'),
        ('i', 'Dunn'),
        ('j', 'Other')
    ])

