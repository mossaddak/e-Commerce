# Generated by Django 4.0.4 on 2022-08-12 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0019_follow_user_followers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Home', models.CharField(max_length=250)),
                ('Area', models.CharField(max_length=250)),
                ('PostOffice', models.CharField(max_length=250)),
                ('Upzilla', models.CharField(max_length=250)),
                ('Zilla', models.CharField(max_length=250)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddresRelatedName', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
