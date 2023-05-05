from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Direccion)
admin.site.register(Proveedor)
admin.site.register(Factura)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Registro_Solicitud)