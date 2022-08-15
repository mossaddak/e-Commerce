# Generated by Django 4.0.4 on 2022-06-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0008_products_total_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available_color',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]