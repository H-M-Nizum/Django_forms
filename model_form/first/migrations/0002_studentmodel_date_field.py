# Generated by Django 4.2.7 on 2023-12-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='date_field',
            field=models.DateField(default='2023-11-11'),
        ),
    ]