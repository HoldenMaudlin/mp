# Generated by Django 2.2.2 on 2019-06-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0006_auto_20190622_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='completion_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
