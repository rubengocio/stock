# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-02 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0024_auto_20180902_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='razon_social',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
