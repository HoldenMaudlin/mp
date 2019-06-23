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
    category = models.CharField(default='1', max_length=40, choices=[
        (1, 'Venice'), 
        (2, 'Sepulveda'), 
        (3, 'Washington'), 
        (4, 'LaCienega'), 
        (5, 'Overland'), 
        (6, 'Robertson'), 
        (7, 'Jefferson'),
        (8, 'W. Adams'),
        (9, 'Dunn'),
        (10, 'Other')
    ])

