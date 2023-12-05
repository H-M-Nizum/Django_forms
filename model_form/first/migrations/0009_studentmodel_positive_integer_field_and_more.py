# Generated by Django 4.2.7 on 2023-12-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_studentmodel_positive_big_integer_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='positive_integer_field',
            field=models.PositiveIntegerField(default=34),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='positive_small_integer_field',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]