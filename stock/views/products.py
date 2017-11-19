# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from stock.forms import ProductForm, InventoryForm
from stock.models import Producto, Categoria, Marca, Inventario


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
        product_form = ProductForm()
        inventory_form = InventoryForm()

        context = {
            'title': 'Producto',
            'product_form': product_form,
            'inventory_form':inventory_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        inventory_form = InventoryForm(data=request.POST)
        product_form = ProductForm(data=request.POST)

        if inventory_form.is_valid() and product_form.is_valid():
            object = inventory_form.save(commit=False)

            object.created_user = request.user
            object.save()

            object2 = product_form.save(commit=False)
            object2.created_user = request.user
            object2.save()

            return HttpResponseRedirect(reverse('product-list'))
        context = {
            'product_form': product_form,
            'inventory_form':inventory_form
        }

        return render(request, self.template_name, context)


class ProductUpdateView(View):
    template_name = "stock/product_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Inventario.objects.get(pk=pk)

        inventory_form = InventoryForm(instance=object)
        product_form = ProductForm(instance=object.producto)

        context = {
            'title': 'Producto',
            'inventory_form': inventory_form,
            'product_form': product_form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        object = Inventario.objects.get(pk=pk)

        inventory_form = InventoryForm(data=request.POST, instance=object)
        product_form = ProductForm(data=request.POST, instance=object.producto)

        if inventory_form.is_valid() and product_form.is_valid():
            inventory_form.save()
            product_form.save()

            return HttpResponseRedirect(reverse('product-list'))
        context = {
            'inventory_form': inventory_form,
            'product_form': product_form
        }

        return render(request, self.template_name, context)


class ProductDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Inventario.objects.get(pk=pk)
        object.delete()
        return HttpResponseRedirect(reverse('product-list'))