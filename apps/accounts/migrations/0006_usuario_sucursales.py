# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_usuario_sucursales'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sucursales',
            field=models.ManyToManyField(to='accounts.Sucursal'),
        ),
    ]
