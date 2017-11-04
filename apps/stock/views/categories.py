# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views import View
from apps.stock.models import Categoria
from django.shortcuts import render
from apps.stock.forms import CategoryForm
from django.core.urlresolvers import reverse


class CategoryListView(View):
    template_name = "stock/generic_list.html"

    def get(self, request,  *args, **kwargs):
        categorias = Categoria.objects.all()

        modificar = reverse('category-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('category-remove', kwargs={'pk': 1}).replace('/1','')

        context = {
            'title': 'Categorias',
            'list': categorias,
            'cols': ['Nombre', 'Descripción'],
            'modificar': modificar,
            'eliminar': eliminar,
        }

        return render(request, self.template_name, context)


class CategoryCreateView(View):
    template_name = "stock/generic_form.html"

    def get(self, request, *args, **kwargs ):
        form = CategoryForm()

        context = {
            'title': 'Categoria',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = CategoryForm(data=request.POST)

        if form.is_valid():
            provider = form.save(commit=False)

            provider.created_user = request.user
            provider.save()

            return HttpResponseRedirect(reverse('category-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class CategoryUpdateView(View):
    template_name = "stock/generic_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        category = Categoria.objects.get(pk=pk)

        form = CategoryForm(instance=category)

        context = {
            'title': 'Categoria',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        category = Categoria.objects.get(pk=pk)

        form = CategoryForm(data=request.POST, instance=category)

        if form.is_valid():
            provider = form.save(commit=False)

            provider.created_user = request.user
            provider.save()

            return HttpResponseRedirect(reverse('category-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class CategoryDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        category = Categoria.objects.get(pk=pk)
        category.delete()
        return HttpResponseRedirect(reverse('category-list'))