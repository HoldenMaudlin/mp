from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Listing(models.Model):
    # Locations
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, default='Culver City')
    zipcode = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    # Details
    price = models.IntegerField(default=0)
    lot_size = models.IntegerField(default=0, blank=True)
    building_size = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    in_escrow = models.BooleanField(default=False)
    # Additional info
    description = models.CharField(max_length=400)
    main_image = models.ImageField(upload_to='images')
    flier = models.FileField(upload_to='fliers')

    class Meta:
        abstract=True


class Sale(Listing):
    in_escrow = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def priceAddOn(self):
        return ""

class SaleImage(models.Model):
    property = models.ForeignKey(Sale, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField()
