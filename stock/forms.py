# -*- coding: utf-8 -*-
from random import choice
from django import forms
from .models import Cliente, Proveedor, Categoria, Marca, UnidadMedida, Producto, Caja


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = ('usuario', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-material',
                'required': 'required'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'razon_social': forms.TextInput(attrs={
                'class': 'input-material',
            }),
            'documento': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-material'
            }),
            'iva': forms.TextInput(attrs={
                'class': 'input-material'
            }),
        }


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'razon_social': forms.TextInput(attrs={
                'class': 'input-material',
                'required': 'required'
            }),
            'cuit': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'input-material',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'contacto': forms.TextInput(attrs={
                'class': 'input-material'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-material'
            }),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Categoria
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-material',
                'required': 'required'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'input-material'
            }),
        }


class BrandForm(forms.ModelForm):

    class Meta:
        model = Marca
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-material',
                'required': 'required'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'input-material'
            }),
        }


class MeasurementForm(forms.ModelForm):

    class Meta:
        model = UnidadMedida
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-material',
                'required': 'required'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'input-material'
            }),
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'codigo_barra': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'marca': forms.Select(attrs={
                'class': 'form-control'
            }),
            'unidad_medida': forms.Select(attrs={
                'class': 'form-control'
            }),

            'precio_compra': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'porcentaje_ganacia': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'stock_actual': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'stock_minimo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'stock_maximo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'estante': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fila': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'columna': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class UploadFileForm(forms.Form):
    DELIMITADOR = ((',', 'Coma (,)'), (';', 'Punto y Coma (;)'),('\t', 'Tabulacion'))
    ESCAPE = (('\'', 'Comillas simples (\')'), ('"', 'Comillas dobles (")'),)

    file = forms.FileField()
    delimitador = forms.ChoiceField(choices=DELIMITADOR)
    escape = forms.ChoiceField(choices=ESCAPE)
    saltar_primer_fila = forms.BooleanField(required=False)
    f = forms.FileInput(attrs={
    })


class BoxForm(forms.ModelForm):

    class Meta:
        model = Caja
        exclude = ()

        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'fecha_cierre': forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),
        }



