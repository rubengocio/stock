# -*- coding: utf-8 -*-
from stock.models import Caja

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from stock.forms import CompraForm
from stock.models import Compra, DetalleCompra, Proveedor
from datetime import datetime


class CompraListView(View):
    template_name = "stock/compra_list.html"

    def get(self, request, *args, **kwargs):
        compras = Compra.objects.all()

        context = {
            'compras': compras
        }

        return render(request, self.template_name, context)

class CompraCreateView(View):
    template_name = "stock/compra_form.html"

    def get(self, request, *args, **kwargs):
        form = CompraForm()
        proveedores = Proveedor.objects.all().order_by('razon_social')

        context = {
            'title': 'Compra',
            'form': form,
            'proveedores': proveedores
        }

        return render(request, self.template_name, context)


class CompraUpdateView(View):
    template_name = "stock/compra_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Compra.objects.get(pk=pk)

        form = CompraForm(instance=object)

        context = {
            'title': 'Compra',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        object = Caja.objects.get(pk=pk)

        form = CompraForm(data=request.POST, instance=object)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('compra-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class CompraDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Compra.objects.get(pk=pk)
        object.delete()
        return HttpResponseRedirect(reverse('compra-list'))