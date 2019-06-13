from django.urls import path, include
from django.http import HttpResponseRedirect
from completedtransactions import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('sold/', views.sold, name='sold'),
    path('leased/', views.leased, name='leased')
]