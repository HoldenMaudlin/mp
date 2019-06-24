from django.shortcuts import render
from completedtransactions.models import CompletedTransactions
from sale.models import Sale
from lease.models import Lease
import json
from decouple import config
import os

def getProperyCoords(props):
    coords = []
    for prop in props:
        coords.append({
            'lat': str(prop.latitude),
            'lng': str(prop.longitude),
            'address': prop.address,
        })
    return coords

def index(request):
    coords = {}

    if 'GOOGLE_API_KEY' in os.environ:
        GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
    else:
        GOOGLE_API_KEY = config('GOOGLE_API_KEY')

    # All listing objects
    for_lease = Lease.objects.filter(completed=False)
    for_sale = Sale.objects.filter(completed=False)
    leased = CompletedTransactions.objects.filter(transaction="Leased")
    sold = CompletedTransactions.objects.filter(transaction="Sold")

    coords['for_lease'] = getProperyCoords(for_lease)
    coords['for_sale'] = getProperyCoords(for_sale)
    coords['sold'] = getProperyCoords(sold)
    coords['leased'] = getProperyCoords(leased)

    json_coords = json.dumps(coords)

    context = {
        'props': json_coords,
        'GOOGLE_API_KEY': GOOGLE_API_KEY
    }
    return render(request, 'map/index.html', context)