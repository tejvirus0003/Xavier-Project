# Generated by Django 3.0.4 on 2020-04-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20200428_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ_type_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_a', models.CharField(max_length=50)),
                ('option_b', models.CharField(max_length=50)),
                ('option_c', models.CharField(max_length=50)),
                ('option_d', models.CharField(max_length=50)),
                ('correct_option', models.CharField(max_length=1)),
            ],
        ),
    ]
