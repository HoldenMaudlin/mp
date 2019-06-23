from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Lease
from django.db.models import Q 
import os
from decouple import config

# Create your views here.


def index(request):
    all_curr_leases = Lease.objects.filter(completed=False)
    recent_leases = Lease.objects.filter(completed=True).order_by('-id')
    context = {
        'sale': False,
        'page': 'Lease',
        'current_properties': all_curr_leases,
        'recent_properties': recent_leases,
        'complete': 'Leased',
    }
    return render(request, 'sale/index.html', context)


def leases(request, Lease_id):
    if 'GOOGLE_API_KEY' in os.environ:
        GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
    else:
        GOOGLE_API_KEY = config('GOOGLE_API_KEY')
    try:
        req_sale = Lease.objects.get(pk=Lease_id)
    except Lease.DoesNotExist:
        raise Http404("Lease listing does not exist.")
    context = {
        'sale': req_sale,
        'page': 'Lease',
        'complete': 'Leased',
        'GOOGLE_API_KEY': GOOGLE_API_KEY,
        'images': getLeasePictures(Lease_id),
        'lat': req_lease.latitude,
        'lng': req_lease.longitude,
    }
    return render(request, 'sale/sale.html', context)

def getLeasePictures(prop_id):
    return Lease.objects.get(pk=prop_id).images.all()