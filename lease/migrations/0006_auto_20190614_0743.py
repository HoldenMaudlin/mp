# Generated by Django 2.2.2 on 2019-06-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0005_remove_lease_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lease',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='lease',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
