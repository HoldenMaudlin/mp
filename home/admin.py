from django.contrib import admin
from .models import TransactionCount
# Register your models here.

class TransactionCountAdmin(admin.ModelAdmin):
    search_fields=['sold', 'leased']

admin.site.register(TransactionCount, TransactionCountAdmin)
