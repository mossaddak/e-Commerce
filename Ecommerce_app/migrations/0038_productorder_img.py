# Generated by Django 4.0.4 on 2022-07-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0037_productorder_createddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]