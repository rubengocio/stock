# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from stock.forms import ProductForm
from stock.models import Producto, Categoria, Marca


class ProductListView(View):
    template_name = "stock/product_list.html"

    def get(self, request,  *args, **kwargs):
        product = Producto.objects.all()

        list_categories = Categoria.objects.filter(
            id__in=product.values_list('categoria__id', flat=True).distinct()
        ).order_by('nombre')

        list_brand = Marca.objects.filter(
            id__in=product.values_list('marca__id', flat=True).distinct()
        ).order_by('nombre')

        modificar = reverse('product-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('product-remove', kwargs={'pk': 1}).replace('/1','')

        context = {
            'title': 'Productos',
            'modificar': modificar,
            'eliminar': eliminar,
            'list_categories': list_categories,
            'list_brand': list_brand,
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