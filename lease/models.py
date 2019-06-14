from sale.models import Listing
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Lease(Listing):
    lease_type = models.CharField(max_length=10, choices=[('NNN', 'NNN'), ('MG', 'MG')])
