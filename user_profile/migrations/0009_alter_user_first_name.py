# Generated by Django 4.0.4 on 2022-06-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_remove_user_fname_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='exit', max_length=150, verbose_name='first name'),
            preserve_default=False,
        ),
    ]
