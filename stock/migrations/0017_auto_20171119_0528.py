# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 05:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20171119_0252'),
        ('stock', '0016_auto_20171119_0414'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventario',
            unique_together=set([('sucursal', 'producto')]),
        ),
    ]
