from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from decouple import config
import os

if 'USER_NAME' in os.environ:
    USER_NAME = os.environ['USER_NAME']
    USER_EMAIL = os.environ['USER_EMAIL']
    USER_PASSWORD = os.environ['USER_PASSWORD']
else:
    USER_NAME = config('USER_NAME')
    USER_EMAIL = config('USER_EMAIL')
    USER_PASSWORD = config('USER_PASSWORD')

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=USER_NAME).exists():
            User.objects.create_superuser(USER_NAME, USER_EMAIL, USER_PASSWORD)
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
        if User.objects.filter(username="holden.maudlin"):
            User.objects.filter(username="holden.maudlin").delete()