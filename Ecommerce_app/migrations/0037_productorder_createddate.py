# Generated by Django 4.0.4 on 2022-07-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0036_productorder_shipping_productorder_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='createdDate',
            field=models.DateField(auto_now=True),
        ),
    ]
