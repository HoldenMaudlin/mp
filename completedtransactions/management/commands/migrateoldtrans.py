from django.core.management.base import BaseCommand, CommandError
from completedtransactions.models import CompletedTransactions
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        if CompletedTransactions.objects.count() == 0:
            print("there were zero")
            data = csv.DictReader(open('./data/pasttransactions.csv', encoding='utf-8-sig'))
            for row in data:
                print(row)
                CompletedTransactions.objects.create(
                    longitude=row['LONGITUDE'],
                    latitude=row['LATITUDE'],
                    transaction=row['TRANSACTION'],
                    address=row['ADDRESS'],
                    transaction_type=row['TYPE']
                )