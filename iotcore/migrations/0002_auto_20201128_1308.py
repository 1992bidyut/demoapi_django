# Generated by Django 3.1.3 on 2020-11-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchbox',
            name='state',
            field=models.IntegerField(max_length=10),
        ),
    ]
