# Generated by Django 4.0.4 on 2022-07-05 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0013_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_quantity',
        ),
    ]
