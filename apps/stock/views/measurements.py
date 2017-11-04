# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views import View
from apps.stock.models import UnidadMedida
from django.shortcuts import render
from apps.stock.forms import MeasurementForm
from django.core.urlresolvers import reverse


class MeasurementListView(View):
    template_name = "stock/generic_list.html"

    def get(self, request,  *args, **kwargs):
        measurements = UnidadMedida.objects.all()

        modificar = reverse('measurement-edit', kwargs={'pk': 1}).replace('/1','')
        eliminar = reverse('measurement-remove', kwargs={'pk': 1}).replace('/1','')

        context = {
            'title': 'Unidades de medida',
            'list': measurements,
            'cols': ['Nombre', 'Descripción'],
            'modificar': modificar,
            'eliminar': eliminar,
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