from sale.models import Listing
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Lease(Listing):
    lease_type = models.CharField(max_length=10, choices=[('NNN', 'NNN'), ('MG', 'MG'), ('FSG', 'FSG')], blank=True)

    def priceAddOn(self):
        return " per month/" + self.lease_type

    def listing_title(self):
        return "Rent:"

class LeaseImage(models.Model):
    property = models.ForeignKey(Lease, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField()
    imagedescription = models.CharField(max_length=100, blank=True)
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.property.address