# Generated by Django 2.2.2 on 2019-06-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0007_auto_20190622_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='completion_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='lease',
            name='lease_type',
            field=models.CharField(blank=True, choices=[('NNN', 'NNN'), ('MG', 'MG'), ('FSG', 'FSG')], max_length=10),
        ),
    ]
