from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Direccion)
admin.site.register(Proveedor)
admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(Registro_Solicitud)