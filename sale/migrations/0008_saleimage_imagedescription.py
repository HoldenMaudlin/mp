# Generated by Django 2.2.2 on 2019-06-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0007_auto_20190621_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleimage',
            name='imagedescription',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]