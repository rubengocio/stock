# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedManyToManyField

# Create your models here.
class Empresa(models.Model):
    razon_social = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return u'%s' % (self.razon_social)


class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa)
    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return u'%s - %s' % (self.empresa, self.direccion)


class Perfil(models.Model):
    user = models.OneToOneField(User)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa)
    sucursales = ChainedManyToManyField(Sucursal,
                                   chained_field='empresa',
                                   chained_model_field='empresa',
                                   #auto_choose=False
                                   )
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    @property
    def get_sucursales(self):
        return self.sucursales


