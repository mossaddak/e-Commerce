# Generated by Django 4.0.4 on 2022-07-12 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecommerce_app', '0018_alter_products_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductREVIEWS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, max_length=250, null=True)),
                ('feedBACK', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productREVIEWrelatedNAME', to='Ecommerce_app.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userREVIEW', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
