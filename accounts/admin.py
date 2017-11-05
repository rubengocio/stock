from django.contrib import admin
from .models import Empresa, Sucursal, Perfil

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Perfil)