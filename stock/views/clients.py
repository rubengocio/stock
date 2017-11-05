# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views import View



# Create your views here.
from stock.forms import ClienteForm
from stock.models import Cliente


@login_required
def home(request):
    template = loader.get_template('stock/index.html')
    return HttpResponse(template.render({}, request))


class ClientListView(View):
    template_name = "stock/cliente_list.html"

    def get(self, request,  *args, **kwargs):

        clientes = Cliente.objects.all()

        context = {
            'clientes': clientes
        }

        return render(request, self.template_name, context)


class ClientCreateView(View):
    template_name = "stock/cliente_form.html"
    form = ClienteForm()

    def get(self, request,  *args, **kwargs):
        form = ClienteForm()

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request,  *args, **kwargs):
        form = ClienteForm(data=request.POST)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()

            return HttpResponseRedirect(reverse('client-list'))

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ClientUpdateView(View):
    template_name = "stock/cliente_form.html"

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        client = Cliente.objects.get(pk=pk)

        form = ClienteForm(instance=client)

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Cliente.objects.get(pk=pk)

        form = ClienteForm(data=request.POST, instance=client)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('client-list'))

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class ClientDeleteView(View):

    def get(self, request, *args, **kwargs ):
        pk = kwargs.get('pk')
        client = Cliente.objects.get(pk=pk)
        client.delete()
        return HttpResponseRedirect(reverse('client-list'))


def register(request):
    template_name = 'stock/register.html'

    if request.method == 'POST':
        user = User()

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = username
        password = request.POST.get('password')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.set_password(password)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            template_name = 'stock/index.html'

    return render(request, template_name)