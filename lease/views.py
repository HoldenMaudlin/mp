from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Lease
from django.db.models import Q

# Create your views here.


def index(request):
    all_curr_leases = Lease.objects.filter(completed=False)
    recent_leases = Lease.objects.filter(completed=True).order_by('-id')
    context = {
        'sale': False,
        'page': 'Lease',
        'current_properties': all_curr_leases,
        'recent_properties': recent_leases,
    }
    return render(request, 'sale/index.html', context)


def leases(request, Lease_id):
    try:
        req_sale = Lease.obects.get(pk=Lease_id)
    except Lease.DoesNotExist:
        raise Http404("Lease listing does not exist.")
    context = {
        'sale': req_sale,
    }
    return render(request, 'sale/sale.html', context)
