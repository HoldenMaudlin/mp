from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Sale
from django.db.models import Q

# Create your views here.
 

def index(request):
    all_curr_sales = Sale.objects.filter(completed=False).filter(in_escrow=False)
    all_in_escrows = Sale.objects.filter(in_escrow=True)
    recent_sales = Sale.objects.filter(completed=True).order_by('-id')
    context = {
        'sale': True,
        'page': 'Sale',
        'current_properties': all_curr_sales,
        'escrow_properties': all_in_escrows,
        'recent_properties': recent_sales,
    }
    return render(request, 'sale/index.html', context)



def sales(request, Sale_id):
    try:
        req_sale = Sale.objects.get(pk=Sale_id)
    except Sale.DoesNotExist:
        raise Http404("Sale listing does not exist.")
    context = {
        'sale': req_sale, 
    }
    return render(request, 'sale/sale.html', context)
