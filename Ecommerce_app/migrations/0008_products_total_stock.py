# Generated by Django 4.0.4 on 2022-06-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0007_auto_20220604_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='total_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]