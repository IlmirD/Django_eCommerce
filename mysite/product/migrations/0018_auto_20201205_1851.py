# Generated by Django 3.0.6 on 2020-12-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20201205_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='image',
            field=models.ImageField(upload_to='marketing_category/'),
        ),
        migrations.AlterField(
            model_name='newarrival',
            name='image',
            field=models.ImageField(upload_to='marketing_category/'),
        ),
        migrations.AlterField(
            model_name='saleoff',
            name='image',
            field=models.ImageField(upload_to='marketing_category/'),
        ),
    ]