# Generated by Django 4.0.4 on 2022-07-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0034_productorder_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='Phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]