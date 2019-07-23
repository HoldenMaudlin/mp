from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Lease
from django.db.models import Q 
import os
import time
from decouple import config
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    if (request.is_ajax()):
        time.sleep(.4)
    all_curr_leases = Lease.objects.filter(completed=False).filter(in_escrow=False).order_by('rank')
    recent_leases = Lease.objects.filter(completed=True).order_by('-completion_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(recent_leases, 9)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    context = {
        'sale': False,
        'page': 'Lease',
        'current_properties': all_curr_leases,
        'recent_properties': recent_leases,
        'complete': 'LEASED',
        'numbers': numbers,
    }
    return render(request, 'sale/sold.html', context)




def leases(request, slug, Lease_id):
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
        'complete': 'LEASED',
        'GOOGLE_API_KEY': GOOGLE_API_KEY,
        'images': getLeasePictures(Lease_id),
        'lat': req_sale.latitude,
        'lng': req_sale.longitude,
    }
    return render(request, 'sale/sale.html', context)

def getLeasePictures(prop_id):
    return Lease.objects.get(pk=prop_id).images.all().order_by('rank')