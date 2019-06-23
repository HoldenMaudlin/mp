from django.contrib import admin
from .models import CompletedTransactions
# Register your models here.


class CompletedTransactionsAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ['address', 'transaction', 'category']
    search_fields = ['address', 'transaction', 'category']

admin.site.register(CompletedTransactions, CompletedTransactionsAdmin)
