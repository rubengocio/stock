# -*- coding: utf-8 -*-
from random import choice
from django import forms
from datetime import datetime

from commons import ErrList
from .models import Cliente, Proveedor, Categoria, Marca, UnidadMedida, Producto, Caja, Inventario, Compra, \
    ESTADO_COMPRA, PORC_IVA, Gasto, MESES


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = ('usuario', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'razon_social': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'documento': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'iva': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'razon_social': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'cuit': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'contacto': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Categoria
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList


class BrandForm(forms.ModelForm):

    class Meta:
        model = Marca
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList

class MeasurementForm(forms.ModelForm):

    class Meta:
        model = UnidadMedida
        exclude = ('created_user', 'created_date', 'updated_date')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(MeasurementForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList

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
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList


class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventario
        exclude = ('created_user', 'created_date', 'updated_date', 'sucursal', 'producto')

        widgets = {
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

    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList


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
        exclude = ('usuario',)

        widgets = {
            'fecha_inicio': forms.DateTimeInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control'}
            ),
            'fecha_cierre': forms.DateTimeInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control'},

            ),
            'monto_inicio': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'monto_cierre': forms.TextInput(
                attrs={'class': 'form-control'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(BoxForm, self).__init__(*args, **kwargs)
        self.error_class = ErrList


class GastoForm(forms.ModelForm):
    gastos = Gasto.objects.all()

    anios = []
    anios.append((str(datetime.now().year),str(datetime.now().year)))
    for gasto in gastos:
        anios.append((str(gasto.created_date__year),str(gasto.created_date__year)))

    anios = list(set(anios))

    anio = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
        choices=anios,
        label=u'Año'
    )
    mes = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=MESES,

    )


    class Meta:
        model = Gasto
        exclude = ()

        widgets = {

            'created_date': forms.DateInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'disabled': 'true',
                                    },

            ),
            'comprobante': forms.Select(attrs={'class': 'form-control'}),
            'nro_comprobante': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        exclude = ('usuario', 'created_date', 'updated_date' )


    estado = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'disabled': 'true',
            }
        ),
        choices=ESTADO_COMPRA
    )

    iva = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=PORC_IVA

    )
