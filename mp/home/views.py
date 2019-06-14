from django.shortcuts import render
from sale.models import Sale
from lease.models import Lease
from itertools import chain

def index(request):
    template = 'home/index.html'
    sales = Sale.objects.filter(featured=True)
    title = 'Featured Property' if  sales.count() < 2 else 'Featured Properties'
    context = {
        'featured_properties': sales,
        'title': title
    }
    return render(request, template, context)

