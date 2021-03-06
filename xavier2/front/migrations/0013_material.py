# Generated by Django 3.0.4 on 2021-04-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0012_remove_announcement_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New material', max_length=30)),
                ('topic', models.TextField()),
                ('file', models.FileField(upload_to='materials')),
                ('tag', models.CharField(default=None, max_length=7)),
            ],
        ),
    ]
