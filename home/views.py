from django.shortcuts import render
from sale.models import Sale
from lease.models import Lease
from itertools import chain

def getProps():
    props = []
    sales = Sale.objects.filter(featured=True)
    for sale in sales:
        props.append({
            'title': 'Sale',
            'id': sale.id,
            'main_image': sale.main_image,
            'city': sale.city,
            'zipcode': sale.zipcode,
            'priceAddOn': sale.priceAddOn,
            'price': sale.price,
            'address': sale.address,
            'building_size': sale.building_size,
            'footage': sale.footage,
            'lot_size': sale.lot_size,
            'listing_title': sale.listing_title,
            'getUrl': sale.getUrl,
    })
    leases = Lease.objects.filter(featured=True)
    for sale in leases:
        props.append({
            'title': 'Lease',
            'id': sale.id,
            'main_image': sale.main_image,
            'address': sale.address,
            'city': sale.city,
            'zipcode': sale.zipcode,
            'priceAddOn': sale.priceAddOn,
            'price': sale.price,
            'building_size': sale.building_size,
            'footage': sale.footage,
            'lot_size': sale.lot_size,
            'listing_title': sale.listing_title,
            'getUrl': sale.getUrl
    })
    return props

def index(request):
    template = 'home/index.html'
    props = getProps()
    title = 'Featured Property' if len(props) < 2 else 'Featured Properties'
    context = {
        'featured_properties': props,
        'title': title
    }
    return render(request, template, context)

