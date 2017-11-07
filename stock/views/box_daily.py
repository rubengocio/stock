# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from stock.forms import BoxForm


class BoxView(View):

    def get(self, request, *args, **kwargs):
        form = BoxForm()
        context = {
            'title': 'Caja diaria',
            'form': form,
        }

        return render(request, 'stock/box_form.html', context)