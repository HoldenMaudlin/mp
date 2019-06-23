from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CompletedTransactions
from sale.models import Sale
from lease.models import Lease
import operator
from django.db.models import Q

def sold(request):
    template = 'completedtransactions/index.html'
    transactions = CompletedTransactions.objects.filter(transaction="Sold").order_by('category')
    context = {
        'title': 'Sold',
        'subtitle': 'Sales',
        'transactions': transactions,
    }
    return render(request, template, context)

def leased(request):
    template = 'completedtransactions/index.html'
    transactions = CompletedTransactions.objects.filter(transaction="Leased").order_by('category')
    leases = Lease.objects.filter(completed=True)
    context = {
        'title': 'Leased',
        'subtitle': 'Leases',
        'transactions': transactions
    }
    return render(request, template, context)

def redirect(request):
    return HttpResponseRedirect('sold/')