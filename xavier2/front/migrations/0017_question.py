# Generated by Django 3.0.4 on 2021-04-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0016_auto_20210417_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('a1', models.CharField(max_length=1)),
                ('a2', models.CharField(max_length=1)),
                ('a3', models.CharField(max_length=1)),
                ('a4', models.CharField(max_length=1)),
                ('correct', models.CharField(max_length=1)),
            ],
        ),
    ]
