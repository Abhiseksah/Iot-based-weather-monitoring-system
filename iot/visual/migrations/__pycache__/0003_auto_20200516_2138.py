# Generated by Django 3.0.5 on 2020-05-16 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iotdata',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 21, 38, 0, 586914)),
        ),
    ]