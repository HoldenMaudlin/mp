from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Sale
from django.db.models import Q

# Create your views here.


def index(request):
    all_for_sales = Sale.objects.all()
    all_in_escrows = Sale.objects.filter(in_escrow=True)
    recent_sales = Sale.objects.filter(completed=True).order_by('-id')
    context = {
        'sale': True,
        'page': 'Sale',
        'all_for_sales': all_for_sales,
        'all_in_escrows':  all_in_escrows,
        'recent_sales': recent_sales,
    }
    return render(request, 'sale/index.html', context)


def sales(request, Sale_id):
    try:
        req_sale = Sale.objects.get(pk=Sale_id)
    except Sale.DoesNotExist:
        raise Http404("Listing does not exist.")
    context = {
        'sale': req_sale,
    }
    return render(request, 'sale/sale.html', context)
