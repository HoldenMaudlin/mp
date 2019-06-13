from django.shortcuts import render
from django.http import HttpResponseRedirect

def sold(request):
    template = 'completedtransactions/index.html'
    context = {}
    print('hi')
    return render(request, template, context)

def leased(request):
    template = 'completedtransactions/index.html'
    context = {}
    print('hi')
    return render(request, template, context)
    
def redirect(request):
    return HttpResponseRedirect('sales/')