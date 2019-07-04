from django.urls import path

from . import views
from .models import Lease
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>,<int:Lease_id>/', views.leases, name='lease'),
]
