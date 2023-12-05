# Generated by Django 4.2.7 on 2023-12-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_studentmodel_float_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='integer_field',
            field=models.IntegerField(default=23),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='json_field',
            field=models.JSONField(default={}),
        ),
    ]
