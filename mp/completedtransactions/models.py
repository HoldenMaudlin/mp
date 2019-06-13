from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class CompletedTransactions(models.Model):
    # Location
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, default='Culver City')
    zipcode = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    transaction = models.CharField(max_length=20, choices=[('Leased', 'Leased'), ('Sold', 'Sold')])

