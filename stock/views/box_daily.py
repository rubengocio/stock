# -*- coding: utf-8 -*-
from stock.models import Caja

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from stock.forms import BoxForm
from stock.models import Caja
from datetime import datetime


class BoxListView(View):
    template_name = "stock/box_list.html"

    def get(self, request, *args, **kwargs):
        boxes = Caja.objects.all()

        context = {
            'boxes': boxes
        }

        return render(request, self.template_name, context)

class BoxCreateView(View):
    template_name = "stock/box_form.html"

    def get(self, request, *args, **kwargs):
        form = BoxForm()

        context = {
            'title': 'Caja',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BoxForm(data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('box-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class BoxUpdateView(View):
    template_name = "stock/box_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Caja.objects.get(pk=pk)

        form = BoxForm(instance=object)

        context = {
            'title': 'Caja diaria',
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        object = Caja.objects.get(pk=pk)

        form = BoxForm(data=request.POST, instance=object)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('box-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class BoxCloseView(View):
    template_name = "stock/box_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Caja.objects.get(pk=pk)

        form = BoxForm(instance=object)

        context = {
            'title': 'Caja diaria',
            'action': 'close',
            'current_date': datetime.now,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        object = Caja.objects.get(pk=pk)

        form = BoxForm(data=request.POST, instance=object)

        if form.is_valid():
            caja=form.save(commit=False)
            caja.usuario=request.user
            caja.save()
            request.session['open_box']=0

            return HttpResponseRedirect(reverse('box-list'))
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

class BoxDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        object = Caja.objects.get(pk=pk)
        object.delete()
        return HttpResponseRedirect(reverse('box-list'))