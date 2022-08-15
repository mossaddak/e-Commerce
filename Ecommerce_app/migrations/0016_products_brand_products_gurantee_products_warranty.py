# Generated by Django 4.0.4 on 2022-07-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0015_products_moreinfo_alter_products_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='gurantee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='warranty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]