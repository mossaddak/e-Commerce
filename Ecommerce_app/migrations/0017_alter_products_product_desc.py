# Generated by Django 4.0.4 on 2022-07-10 19:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0016_products_brand_products_gurantee_products_warranty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
