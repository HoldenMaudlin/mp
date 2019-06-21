from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Sale, SaleImage
from django.db.models import Q
import os
from decouple import config

# Create your views here.
 

def index(request):
    all_curr_sales = Sale.objects.filter(completed=False).filter(in_escrow=False)
    all_in_escrows = Sale.objects.filter(in_escrow=True)
    recent_sales = Sale.objects.filter(completed=True).order_by('-completion_date')
    context = {
        'sale': True,
        'page': 'Sale',
        'current_properties': all_curr_sales,
        'escrow_properties': all_in_escrows,
        'recent_properties': recent_sales,
        'complete': 'Sold',
    }
    return render(request, 'sale/index.html', context)



def sales(request, Sale_id):
    if 'GOOGLE_API_KEY' in os.environ:
        GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
    else:
        GOOGLE_API_KEY = config('GOOGLE_API_KEY')
    try:
        req_sale = Sale.objects.get(pk=Sale_id)
    except Sale.DoesNotExist:
        raise Http404("Sale listing does not exist.")
    images = getSalePictures(Sale_id)
    context = {
        'sale': req_sale, 
        'page': 'Sale',
        'complete': 'Sold',
        'GOOGLE_API_KEY': GOOGLE_API_KEY,
        'images': images,
    }
    return render(request, 'sale/sale.html', context)

def getSalePictures(prop_id):
    pictures = []
    prop = Sale.objects.get(pk=prop_id)
    print(prop)
    images = prop.images.all()
    for pic in images:
        pictures.append({
            'image': pic.image,
            'desc': pic.imagedescription,
        })
    return images