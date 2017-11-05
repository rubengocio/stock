# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from stock.forms import MeasurementForm
from stock.models import UnidadMedida


class MeasurementListView(View):
    template_name = "stock/generic_list.html"

    def get(self, request,  *args, **kwargs):
        modificar = reverse('measurement-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('measurement-remove', kwargs={'pk': 1}).replace('/1','')
        url_list = reverse('api_measure_list')

        context = {
            'title': 'Unidades de medida',
            'modificar': modificar,
            'eliminar': eliminar,
            'url_list': url_list
        }

        return render(request, self.template_name, context)


class MeasurementCreateView(View):
    template_name = "stock/generic_form.html"

    def get(self, request, *args, **kwargs ):
        form = MeasurementForm()

        context = {
            'title': 'Unidad de medida',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = MeasurementForm(data=request.POST)

        if form.is_valid():
            object = form.save(commit=False)

            object.created_user = request.user
            object.save()

            return HttpResponseRedirect(reverse('measurement-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class MeasurementUpdateView(View):
    template_name = "stock/generic_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = UnidadMedida.objects.get(pk=pk)

        form = MeasurementForm(instance=object)

        context = {
            'title': 'Unidad de medida',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        object = UnidadMedida.objects.get(pk=pk)

        form = MeasurementForm(data=request.POST, instance=object)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('measurement-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class MeasurementDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = UnidadMedida.objects.get(pk=pk)
        object.delete()
        return HttpResponseRedirect(reverse('measurement-list'))