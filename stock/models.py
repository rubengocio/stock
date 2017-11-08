# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import Max


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellido = models.CharField(max_length=200, blank=False, null=False)
    razon_social = models.CharField(max_length=200, blank=False, null=False)
    documento = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    iva = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)
    usuario = models.ForeignKey(User)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=200, blank=False, null=True, unique=True)
    cuit = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return '%s' % (self.razon_social)

    def __unicode__(self):
        return '%s' % (self.razon_social)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False, unique=True)
    descripcion = models.CharField(max_length=100,blank=True, null=True)
    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def __unicode__(self):
        return '%s' % (self.nombre)

    @property
    def get_array_value(self):
        array = []
        array.append(self.nombre)
        array.append(self.descripcion)

        return array


class Marca(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False, unique=True)
    descripcion = models.CharField(max_length=100,blank=True, null=True)
    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def __unicode__(self):
        return '%s' % (self.nombre)

    @property
    def get_array_value(self):
        array = []
        array.append(self.nombre)
        array.append(self.descripcion)

        return array


class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False, unique=True)
    descripcion = models.CharField(max_length=100,blank=True, null=True)
    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def __unicode__(self):
        return '%s' % (self.nombre)

    @property
    def get_array_value(self):
        array = []
        array.append(self.nombre)
        array.append(self.descripcion)

        return array


class Producto(models.Model):
    codigo_barra = models.CharField(max_length=13,blank=True, null=True)
    nombre = models.CharField(max_length=250,blank=False, null=False)
    categoria = models.ForeignKey(Categoria, null=True)
    marca = models.ForeignKey(Marca, null=True)
    unidad_medida = models.ForeignKey(UnidadMedida, null=True)
    precio_compra = models.DecimalField(null=True, max_digits=999999, decimal_places=2)
    porcentaje_ganacia = models.DecimalField(null=True, max_digits=100, decimal_places=2)
    stock_actual = models.DecimalField(null=True, max_digits=999999, decimal_places=2)
    stock_minimo = models.DecimalField(null=True, max_digits=999999, decimal_places=2)
    stock_maximo = models.DecimalField(null=True, max_digits=999999, decimal_places=2)
    estante = models.CharField(null=True, max_length=10)
    fila = models.CharField(null=True, max_length=10)
    columna = models.CharField(null=True, max_length=10)
    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def __unicode__(self):
        return '%s' % (self.nombre)

    @property
    def get_array_value(self):
        array = []
        array.append(self.nombre)
        array.append(self.categoria)
        array.append(self.marca)
        array.append(self.unidad_medida)
        array.append(self.stock_actual)
        array.append(self.estante)
        array.append(self.fila)
        array.append(self.columna)

        return array

    def __get_next_id(self):
        actual = Producto.objects.aggregate(Max("id"))['id__max']
        actual+=1
        return actual

    def __get_codigo_ean(self):
        cod_pais = '779'
        id = '%s' % str(self.id)
        cod_prod = id.rjust(9, '0')
        ean = cod_pais + cod_prod
        ean = '%s%s' % (ean ,self.__get_checksum(ean))
        return ean

    def __get_checksum(self, ean):
        checksum = 0
        for i, digit in enumerate(reversed(ean)):
            checksum += int(digit) * 3 if (i % 2 == 0) else int(digit)

        return (10 - (checksum % 10)) % 10

    @staticmethod
    def is_code_valid(code):
        try:
            ean = code[:12]
            check = code[12:13]
            product = Producto()
            checksum = product.__get_checksum(ean)

            if check == checksum:
                return True
        except:
            pass

        return False

    def save(self, *args, **kwargs):
        super(Producto, self).save(force_insert=False, force_update=False, using=None ,update_fields=None)

        if self.codigo_barra is None or self.codigo_barra == '':
            self.codigo_barra = self.__get_codigo_ean()
            super(Producto, self).save(*args, **kwargs)


class Caja(models.Model):
    fecha_inicio = models.DateTimeField()
    monto_inicio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_cierre = models.DateTimeField()
    monto_cierre = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User)

    def __str__(self):
        return '%s %s %s %s' % (self.fecha_inicio, self.fecha_cierre, self.usuario.first_name, self.usuario.last_name,)




