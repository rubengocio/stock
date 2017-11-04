# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views import View

from apps.stock.models import Producto, Categoria, Marca, UnidadMedida
from django.shortcuts import render
from apps.stock.forms import ProductForm
from django.core.urlresolvers import reverse


class ProductListView(View):
    template_name = "stock/product_list.html"

    def get(self, request,  *args, **kwargs):
        list_objects = Producto.objects.all()
        list_categories = Categoria.objects.all()
        list_brand = Categoria.objects.all()
        list_measure = Categoria.objects.all()

        modificar = reverse('product-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('product-remove', kwargs={'pk': 1}).replace('/1','')

        context = {
            'title': 'Productos',
            'list': list_objects,
            'cols': ['Nombre', 'Categoria', 'Marca', 'Unidad de medida', 'Stock Actual', 'Estante', 'Fila', 'Columna'],
            'modificar': modificar,
            'eliminar': eliminar,
            'list_categories': list_categories,
            'list_brand': list_brand,
            'list_measure': list_measure
        }

        return render(request, self.template_name, context)


class ProductCreateView(View):
    template_name = 'stock/product_form.html'

    def get(self, request, *args, **kwargs ):
        form = ProductForm()

        context = {
            'title': 'Producto',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = ProductForm(data=request.POST)

        if form.is_valid():
            object = form.save(commit=False)

            object.created_user = request.user
            object.save()

            return HttpResponseRedirect(reverse('product-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ProductUpdateView(View):
    template_name = "stock/product_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Producto.objects.get(pk=pk)

        form = ProductForm(instance=object)

        context = {
            'title': 'Producto',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        object = Producto.objects.get(pk=pk)

        form = ProductForm(data=request.POST, instance=object)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('product-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ProductDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Producto.objects.get(pk=pk)
        object.delete()
        return HttpResponseRedirect(reverse('product-list'))