# Generated by Django 4.2.7 on 2023-12-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_studentmodel_decimal_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='email_field',
            field=models.EmailField(default='aaa@gmail.com', max_length=254),
        ),
    ]