from django.contrib import admin
from .models import Cliente, Proveedor, Categoria, Marca, UnidadMedida, Producto, Caja, Inventario, Comprobante, Mes

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Caja)
admin.site.register(Comprobante)
admin.site.register(Mes)

