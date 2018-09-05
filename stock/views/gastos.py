# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import View
from datetime import datetime
from stock.forms import GastoForm
from stock.models import Mes


class GastoCreateView(View):
    template_name = "stock/gasto_form.html"


    def get(self, request, *args, **kwargs):
        form = GastoForm()
        fecha = datetime.now()
        months = Mes.objects.all()
        context = {
            'title': 'Gasto',
            'form': form,
            'now': fecha.strftime('%d/%m/%Y'),
            'month': fecha.month,
            'months': months
        }

        return render(request, self.template_name, context)