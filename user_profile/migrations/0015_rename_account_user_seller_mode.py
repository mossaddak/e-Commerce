# Generated by Django 4.0.4 on 2022-06-24 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0014_alter_user_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account',
            new_name='seller_mode',
        ),
    ]
