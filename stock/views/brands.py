# -*- coding: utf-8 -*-
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from stock.forms import BrandForm
from stock.models import Marca


class BrandListView(View):
    template_name = "stock/generic_list.html"

    def get(self, request,  *args, **kwargs):

        modificar = reverse('brand-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('brand-remove', kwargs={'pk': 1}).replace('/1','')
        url_list = reverse('brand-list')

        page = int(request.GET.get('page', '1'))
        objects = Marca.objects.all()
        paginator = Paginator(objects, 10)
        objects = paginator.page(page)

        context = {
            'title': 'Marcas',
            'modificar': modificar,
            'eliminar': eliminar,
            'url_list': url_list,
            'objects': objects,
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