from django.urls import path

from . import views
from .models import Sale
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Sale_id>', views.sales, name='sale'),
]
