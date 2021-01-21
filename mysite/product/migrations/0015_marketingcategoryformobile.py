# Generated by Django 3.0.6 on 2020-12-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_delete_ficc'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingCategoryForMobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketing_name', models.CharField(blank=True, max_length=100, null=True)),
                ('marketing_image_mobile', models.ImageField(upload_to='marketing_category/')),
            ],
        ),
    ]
