# Generated by Django 3.0.6 on 2020-12-05 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20201205_1417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discount',
            new_name='Marketing',
        ),
        migrations.DeleteModel(
            name='NewArrival',
        ),
        migrations.DeleteModel(
            name='SaleOff',
        ),
    ]
