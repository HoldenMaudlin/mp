# Generated by Django 2.2.2 on 2019-06-13 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(default='Culver City', max_length=50)),
                ('zipcode', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('longitude', models.DecimalField(decimal_places=7, default=0, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=7, default=0, max_digits=10)),
                ('transaction', models.CharField(choices=[('Leased', 'Leased'), ('Sold', 'Sold')], max_length=20)),
            ],
        ),
    ]
