from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Sale(models.Model):
    # Locations
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, default='Culver City')
    zipcode = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    # Details
    price = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    lot_size = models.IntegerField(default=0, blank=True)
    building_size = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    in_escrow = models.BooleanField(default=False)
    # Additional info
    description = models.CharField(max_length=400)
    main_image = models.ImageField(upload_to='images')
    flier = models.FileField(upload_to='fliers')