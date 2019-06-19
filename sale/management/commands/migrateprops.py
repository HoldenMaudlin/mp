from django.core.management.base import BaseCommand, CommandError
from sale.models import Sale
from lease.models import Lease
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        if Sale.objects.count() == 0:
            print("there were zero")
            data = csv.DictReader(open('./data/CurrentListings.csv', encoding='utf-8-sig'))
            for row in data:
                print(row)
                CompletedTransactions.objects.create(
                    longitude=row['LONGITUDE'],
                    latitude=row['LATITUDE'],
                    transaction=row['TRANSACTION'],
                    address=row['ADDRESS'],
                    transaction_type=row['TYPE']
                )