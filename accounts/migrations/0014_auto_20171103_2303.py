# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 02:03
from __future__ import unicode_literals

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_perfil_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='sucursales',
        ),
        migrations.AddField(
            model_name='perfil',
            name='sucursales',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field=b'empresa', chained_model_field=b'empresa', to='accounts.Sucursal'),
        ),
    ]
