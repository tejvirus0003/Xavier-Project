# Generated by Django 3.1.7 on 2021-04-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0019_remove_profile_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.CharField(choices=[('cn', 'Computer Networks'), ('os', 'Operating System'), ('dbms', 'Database Management'), ('ml', 'Machine Learning')], default='cn', max_length=9),
        ),
    ]
