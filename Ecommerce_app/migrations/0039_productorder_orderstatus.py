# Generated by Django 4.0.4 on 2022-08-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0038_productorder_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='OrderStatus',
            field=models.CharField(blank=True, choices=[('Processing', 'Processing'), ('On the way', 'On the way'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=30, null=True),
        ),
    ]