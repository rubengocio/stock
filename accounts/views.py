from django.conf import settings
from django.contrib.auth import authenticate, login as login_
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Perfil


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwords = request.POST.get('password')
        user = authenticate(username=username, password=passwords)
        perfil = Perfil.objects.get(user=user)
        empresa = perfil.empresa.razon_social
        empresa_id=perfil.empresa.id
        sucursales = perfil.sucursales.all()
        open_box = perfil.get_open_box
        json = serializers.serialize('json', sucursales )

        next = request.POST.get('next')
        request.session['sucursales'] = json
        request.session['empresa'] = empresa
        request.session['sucursal'] = sucursales.first().id
        request.session['open_box'] = open_box.id if open_box else 0
        request.session['empresa_id']=empresa_id

        if user:
            login_(request, user)
            redirect_to = settings.LOGIN_REDIRECT_URL
            if next and next != '':
                redirect_to = next

            return redirect(redirect_to)

    return render(request, 'accounts/login.html')

@csrf_exempt
def change_sucursal(request):
    import json
    if request.method == 'POST':
        sucursal = request.POST.get('sucursal', None)

        if sucursal:
            request.session['sucursal'] = sucursal

    return HttpResponse(
        json.dumps({'status': 'ok'}),
        content_type='application/json; charset=UTF-8'
    )