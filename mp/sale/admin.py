from django.contrib import admin
from .models import Sale
from .models import SaleImage
# Register your models here.

admin.site.register(Sale)
admin.site.register(SaleImage)