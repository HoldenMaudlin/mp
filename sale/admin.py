from django.contrib import admin
from .models import Sale
from .models import SaleImage
# Register your models here.

class SaleImageAdmin(admin.ModelAdmin):
    raw_id_fields=("property",)
    autocomplete_fields=['property']

class SaleAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ['address', 'completed', 'rank']
    search_fields = ['address']

admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleImage, SaleImageAdmin)