# Generated by Django 2.2.2 on 2019-06-16 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('completedtransactions', '0003_auto_20190615_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTransactionsSearch',
            fields=[
                ('completedtransactions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='completedtransactions.CompletedTransactions')),
            ],
            bases=('completedtransactions.completedtransactions',),
        ),
    ]
