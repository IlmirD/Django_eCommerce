# Generated by Django 3.0.6 on 2020-12-05 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_marketingcategoryformobile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryForMobile',
            new_name='ProductCategoryForMobile',
        ),
    ]