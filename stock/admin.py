from django.contrib import admin
from .models import Cliente, Proveedor, Categoria, Marca, UnidadMedida, Producto, Caja


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Producto)
admin.site.register(Caja)


