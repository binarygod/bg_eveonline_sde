# Generated by Django 3.1 on 2020-08-27 19:36

import bg_eveonline_sde.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAttributes',
            fields=[
                ('typeID', models.IntegerField(primary_key=True, serialize=False)),
                ('attributeID', models.IntegerField()),
                ('valueInt', models.IntegerField(null=True)),
                ('valueFloat', bg_eveonline_sde.utils.CustomFloatField(null=True)),
            ],
            options={
                'db_table': 'dgmTypeAttributes',
            },
        ),
    ]