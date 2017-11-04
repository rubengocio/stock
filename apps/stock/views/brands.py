# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views import View
from apps.stock.models import Marca
from django.shortcuts import render
from apps.stock.forms import BrandForm
from django.core.urlresolvers import reverse


class BrandListView(View):
    template_name = "stock/generic_list.html"

    def get(self, request,  *args, **kwargs):
        marcas = Marca.objects.all()

        modificar = reverse('brand-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('brand-remove', kwargs={'pk': 1}).replace('/1','')

        context = {
            'title': 'Marcas',
            'list': marcas,
            'cols': ['Nombre', 'Descripción'],
            'modificar': modificar,
            'eliminar': eliminar,
        }

        return render(request, self.template_name, context)


class BrandCreateView(View):
    template_name = "stock/generic_form.html"

    def get(self, request, *args, **kwargs ):
        form = BrandForm()

        context = {
            'title': 'Marca',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = BrandForm(data=request.POST)

        if form.is_valid():
            brand = form.save(commit=False)

            brand.created_user = request.user
            brand.save()

            return HttpResponseRedirect(reverse('brand-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class BrandUpdateView(View):
    template_name = "stock/generic_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        brand = Marca.objects.get(pk=pk)

        form = BrandForm(instance=brand)

        context = {
            'title': 'Marca',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        brand = Marca.objects.get(pk=pk)

        form = BrandForm(data=request.POST, instance=brand)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('brand-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class BrandDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        marca = Marca.objects.get(pk=pk)
        marca.delete()
        return HttpResponseRedirect(reverse('brand-list'))