# Generated by Django 3.0.5 on 2020-05-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iotdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temprature', models.FloatField()),
                ('pressure', models.FloatField()),
                ('altitude', models.FloatField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
