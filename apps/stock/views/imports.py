# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.stock.forms import UploadFileForm
from apps.stock.models import Producto, Categoria, Marca, UnidadMedida
import csv


class ProductImport():
    codigo_barra = ''
    nombre = ''
    precio_compra = ''
    stock_actual = ''
    stock_minimo = ''
    stock_maximo = ''
    categoria = ''
    marca = ''
    unidad_medida = ''
    errores = ''

    @property
    def get_array_value(self):
        array = []
        array.append(self.codigo_barra)
        array.append(self.nombre)
        array.append(self.categoria)
        array.append(self.marca)
        array.append(self.unidad_medida)
        array.append(self.precio_compra)
        array.append(self.stock_actual)
        array.append(self.stock_minimo)
        array.append(self.stock_maximo)
        array.append(self.errores)

        return array


def upload(request):
    template_name = 'stock/importador.html'
    result = []
    errors = []
    columns = ['codigo_barra', 'nombre', 'categoria', 'marca', 'unidad_medida', 'precio', 'stock_actual', 'stock_minimo', 'stock_maximo', 'errores']


    if request.POST and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            delimiter = str(form.cleaned_data['delimitador'])
            escape = str(form.cleaned_data['escape'])
            reader = csv.reader(form.cleaned_data['file'], delimiter=delimiter,  quotechar=escape, quoting=csv.QUOTE_ALL)

            skip = form.cleaned_data['saltar_primer_fila']

            for row in reader:
                if skip is False:
                    error = ''
                    product = ProductImport()

                    try:
                        test = row
                        product.codigo_barra = row[0]
                    except:
                        error = error + ',codigo_barra'

                    try:
                        product.nombre = row[1]
                    except:
                        error = error + ',nombre'

                    try:
                        product.categoria = row[2]
                    except:
                        error = error + ',categoria'

                    try:
                        product.marca = row[3]
                    except:
                        error = error + ',marca'

                    try:
                        product.unidad_medida = row[4]
                    except:
                        error = error + ',unidad_medida'

                    try:
                        product.precio_compra = row[5]
                    except:
                        error = error + ',precio_compra'

                    try:
                        product.stock_actual = row[6]
                    except:
                        error = error + ',stock_actual'

                    try:
                        product.stock_minimo = row[7]
                    except:
                        error = error + ',stock_minimo'

                    try:
                        product.stock_maximo = row[8]
                    except:
                        error = error + ',stock_maximo'

                    product.errores = error

                    result.append(product)
                else:
                    skip = False

            importar(request.user, result)
        else:
            errors = form.errors
    else:
        form = UploadFileForm()

    context = {
        'form': form,
        'result': result[:20],
        'columns': columns,
        'errors': errors
    }

    return render(request, template_name, context)


def importar(user, product_list):
    from decimal import Decimal

    for prod in product_list:
        product = Producto()

        if Producto.is_code_valid(prod.codigo_barra):
            product.codigo_barra = prod.codigo_barra
        else:
            product.codigo_barra = ''

        if Producto.objects.filter(codigo_barra=prod.codigo_barra).exists():
            product = Producto.objects.get(codigo_barra=prod.codigo_barra)

        product.nombre = prod.nombre

        try:
            product.precio_compra = Decimal(prod.precio_compra)
        except:
            product.precio_compra = 0

        try:
            product.stock_actual = Decimal(prod.stock_actual)
        except:
            product.stock_actual = 0

        try:
            product.stock_minimo = Decimal(prod.stock_minimo)
        except:
            product.stock_minimo = 0

        try:
            product.stock_maximo = Decimal(prod.stock_maximo)
        except:
            product.stock_maximo = 0

        try:
            categoria = Categoria.objects.get(nombre=prod.categoria)
        except:
            categoria = Categoria()
            categoria.nombre = prod.categoria
            categoria.created_user = user
            categoria.save()

        try:
            marca = Marca.objects.get(nombre=prod.marca)
        except:
            marca = Marca()
            marca.nombre = prod.marca
            marca.created_user = user
            marca.save()

        try:
            unidad_medida = UnidadMedida.objects.get(nombre=prod.unidad_medida)
        except:
            unidad_medida = UnidadMedida()
            unidad_medida.nombre = prod.unidad_medida
            unidad_medida.created_user = user
            unidad_medida.save()


        product.categoria = categoria
        product.marca = marca
        product.unidad_medida = unidad_medida
        product.created_user = user
        product.save()