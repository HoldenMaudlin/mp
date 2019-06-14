from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="holden.maudlin").exists():
            User.objects.create_superuser("holden.maudlin", "holden.maudlin@gmail.com", "dodgers13")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))