from django.conf import settings
from django.contrib.auth import authenticate, login as login_
from django.shortcuts import render, redirect
from django.core import serializers

# Create your views here.
from .models import Perfil


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwords = request.POST.get('password')
        user = authenticate(username=username, password=passwords)
        perfil = Perfil.objects.get(user=user)
        empresa = perfil.empresa.razon_social
        sucursales = perfil.sucursales.all()

        json = serializers.serialize('json', sucursales )

        next = request.POST.get('next')
        request.session['sucursales'] = json
        request.session['empresa'] = empresa

        if user:
            login_(request, user)
            redirect_to = settings.LOGIN_REDIRECT_URL
            if next and next != '':
                redirect_to = next

            return redirect(redirect_to)

    return render(request, 'accounts/login.html')


