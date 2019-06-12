from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Lease
from django.db.models import Q

# Create your views here.


def index(request):
    all_for_sales = Lease.objects.all()
    recent_sales = Lease.objects.filter(completed=True).order_by('-id')
    context = {
        'sale': False,
        'page': 'Lease',
        'all_for_sales': all_for_sales,
        'recent_sales': recent_sales,
    }
    return render(request, 'sale/index.html', context)


def leases(request, Lease_id):
    try:
        req_sale = Lease.objects.get(pk=Lease_id)
    except Lease.DoesNotExist:
        raise Http404("Listing does not exist.")
    context = {
        'sale': req_sale,
    }
    return render(request, 'sale/sale.html', context)
