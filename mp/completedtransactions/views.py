from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CompletedTransactions

def sold(request):
    template = 'completedtransactions/index.html'
    sales = CompletedTransactions.objects.filter(transaction="Sold")
    context = {
        'transaction_type': 'Sold',
        'transactions': sales,
    }
    return render(request, template, context)

def leased(request):
    template = 'completedtransactions/index.html'
    leases = CompletedTransactions.objects.filter(transaction="Leased")
    context = {
        'transaction_type': 'Sold',
        'transactions': leases
    }
    return render(request, template, context)
    
def redirect(request):
    return HttpResponseRedirect('sold/')