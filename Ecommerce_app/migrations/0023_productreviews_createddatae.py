# Generated by Django 4.0.4 on 2022-07-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0022_alter_productreviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreviews',
            name='createdDatae',
            field=models.DateField(blank=True, null=True),
        ),
    ]