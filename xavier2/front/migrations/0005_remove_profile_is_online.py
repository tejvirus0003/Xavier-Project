# Generated by Django 3.0.4 on 2021-04-13 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_profile_is_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_online',
        ),
    ]
