from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.

class Listing(models.Model):
    # Locations
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, default='Culver City')
    zipcode = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    # Details
    price = models.IntegerField(default=0, blank=True)
    lot_size = models.IntegerField(default=0, blank=True)
    building_size = models.IntegerField(default=0, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    in_escrow = models.BooleanField(default=False, blank=True)
    property_type = models.CharField(max_length=40, default="Owner/User", blank=True)
    completion_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=date.today())
    # Additional info
    description = models.CharField(max_length=400, blank=True)
    main_image = models.ImageField(upload_to='images/', blank=True)
    flier = models.FileField(upload_to='fliers/', blank=True)
    rank = models.IntegerField(default=1)

    def footage():
        return "sq. ft."

    def __str__(self):
        return self.address

    class Meta:
        abstract=True


class Sale(Listing):
    in_escrow = models.BooleanField(default=False, blank=True)
    featured = models.BooleanField(default=False, blank=True)

    def priceAddOn(self):
        return ""

class SaleImage(models.Model):
    property = models.ForeignKey(Sale, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return self.property.address
