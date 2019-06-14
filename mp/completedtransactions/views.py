from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CompletedTransactions
from sale.models import Sale
from lease.models import Lease

def sold(request):
    template = 'completedtransactions/index.html'
    transactions = []
    sales = Sale.objects.filter(completed=True)
    for sale in sales:
        transactions.append({'address': sale.address, 'id': sale.id})
    old_sales = CompletedTransactions.objects.filter(transaction="Sold")
    for sale in old_sales:
        transactions.append({'address': sale.address, 'id': sale.id})
    context = {
        'title': 'Sold',
        'transactions': transactions,
    }
    return render(request, template, context)

def leased(request):
    template = 'completedtransactions/index.html'
    transactions = []
    leases = Lease.objects.filter(completed=True)
    for lease in leases:
        transactions.append({'address': lease.address, 'id': lease.id})
    old_leases = CompletedTransactions.objects.filter(transaction="Leased")
    for lease in old_leases:
        transactions.append({'address': lease.address, 'id': lease.id})
    context = {
        'title': 'Leased',
        'transactions': leases
    }
    return render(request, template, context)

def redirect(request):
    return HttpResponseRedirect('sold/')