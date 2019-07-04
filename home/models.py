from django.db import models

# Create your models here.

class TransactionCount(models.Model):
    sold = models.IntegerField()
    leased = models.IntegerField()

    def save(self):
        if self.id:
           super().save()
        elif TransactionCount.objects.all().count() > 0:
            return 
        else:
            super().save()