# Generated by Django 4.0.4 on 2022-08-10 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0041_remove_productreviews_review_once_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopingcart',
            name='createdDate',
            field=models.DateField(auto_now=True),
        ),
    ]
