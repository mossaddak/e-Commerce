# Generated by Django 4.0.4 on 2022-06-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0011_products_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='created_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]