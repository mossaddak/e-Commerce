# Generated by Django 4.0.4 on 2022-07-11 07:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0017_alter_products_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]