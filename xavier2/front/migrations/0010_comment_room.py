# Generated by Django 3.0.4 on 2021-04-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_auto_20210414_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='room',
            field=models.CharField(default='00000000', max_length=8),
        ),
    ]