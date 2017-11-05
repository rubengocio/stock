# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from stock.forms import ProviderForm
from stock.models import Proveedor


class ProviderListView(View):
    template_name = "stock/provider_list.html"

    def get(self, request,  *args, **kwargs):
        proveedores = Proveedor.objects.all()

        context = {
            'proveedores': proveedores
        }

        return render(request, self.template_name, context)


class ProviderCreateView(View):
    template_name = "stock/provider_form.html"

    def get(self, request, *args, **kwargs ):
        form = ProviderForm()

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = ProviderForm(data=request.POST)

        if form.is_valid():
            provider = form.save(commit=False)

            provider.created_user = request.user
            provider.save()

            return HttpResponseRedirect(reverse('provider_list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ProviderUpdateView(View):
    template_name = "stock/provider_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        provider = Proveedor.objects.get(pk=pk)

        form = ProviderForm(instance=provider)

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        provider = Proveedor.objects.get(pk=pk)

        form = ProviderForm(data=request.POST, instance=provider)

        if form.is_valid():
            provider = form.save(commit=False)

            provider.created_user = request.user
            provider.save()

            return HttpResponseRedirect(reverse('provider_list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ProviderDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        provider = Proveedor.objects.get(pk=pk)
        provider.delete()
        return HttpResponseRedirect(reverse('provider_list'))