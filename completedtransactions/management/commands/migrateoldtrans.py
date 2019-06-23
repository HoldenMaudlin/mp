from django.core.management.base import BaseCommand, CommandError
from completedtransactions.models import CompletedTransactions
import csv

def getCategory(address):
    bank = {1: 'Venice',
        2: 'Sepulveda',
        3: 'Washington',
        4: 'LaCienega',
        5: 'Overland',
        6: 'Robertson',
        7: 'Jefferson',
        8: 'W. Adams',
        9: 'Dunn'
    }
    for key, value in bank.items():
        if value in address:
            return key
    return 10


class Command(BaseCommand):
    def handle(self, *args, **options):
        if CompletedTransactions.objects.count() == 0:
            data = csv.DictReader(open('./data/pasttransactions.csv', encoding='utf-8-sig'))
            for row in data:
                CompletedTransactions.objects.create(
                    longitude=row['LONGITUDE'],
                    latitude=row['LATITUDE'],
                    transaction=row['TRANSACTION'],
                    address=row['ADDRESS'],
                    property_type=row['TYPE'],
                    category=getCategory(row['ADDRESS'])
                )
            self.stdout.write(self.style.SUCCESS('Successfully migrated old props'))
