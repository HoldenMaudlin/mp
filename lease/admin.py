from django.contrib import admin
from .models import Lease, LeaseImage
# Register your models here.

class LeaseImageAdmin(admin.ModelAdmin):
    raw_id_fields=("property",)
    autocomplete_fields=['property']
    list_display = ['property', 'rank']
    search_fields=['property']

class LeaseAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ['address', 'completed', 'rank']
    search_fields = ['address']

admin.site.register(Lease, LeaseAdmin)
admin.site.register(LeaseImage, LeaseImageAdmin)