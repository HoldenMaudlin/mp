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
                if row['SALE'] == '1':
                    Sale.objects.create(
                        longitude=row['LONGITUDE'],
                        latitude=row['LATITUDE'],
                        address=row['ADDRESS'],
                        city=row['CITY'],
                        zipcode=row['ZIPCODE'],
                        completed=row['TRANSACTION'],
                        price=row['PRICE'],
                        description=row['DESCRIPTION'],
                        featured=False,
                        lot_size=row['LOT_SIZE'],
                        building_size=row['BUILDING_SIZE'],
                        property_type=row['TYPE'],
                        in_escrow=False,
                        main_image='soon.jpg'
                    )
                else:
                    Lease.objects.create(
                        longitude=row['LONGITUDE'],
                        latitude=row['LATITUDE'],
                        address=row['ADDRESS'],
                        city=row['CITY'],
                        zipcode=row['ZIPCODE'],
                        completed=row['TRANSACTION'],
                        price=row['PRICE'],
                        description=row['DESCRIPTION'],
                        lot_size=row['LOT_SIZE'],
                        building_size=row['BUILDING_SIZE'],
                        property_type=row['TYPE'],
                        in_escrow=False,
                        main_image='soon.jpg',
                        lease_type='NNN'
                    )
            self.stdout.write(self.style.SUCCESS('Successfully migrated props'))

