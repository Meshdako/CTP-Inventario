from django.urls import path
from .views import *

app_main = "main"

urlpatterns=[
    # URLs Productos
    path('productos/', ProductView.as_view(), name='product_list'),
    path('productos/<int:id>', ProductView.as_view(), name='product_process'),
    # URLs Facturas
    path('facturas/', FacturaView.as_view(), name='factura_list'),
    path('facturas/<int:id>', FacturaView.as_view(), name='factura_process'),
    # URLs Proveedores
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/<int:id>', ProveedorView.as_view(), name='proveedor_process'),
    # URLs Registros
    path('registros/', RegistroView.as_view(), name='registro_list'),
    path('registros/<int:id>', RegistroView.as_view(), name='registro_process'),
    # URLs Plantillas
    path("productos/views", Products, name="productos"),
    path("facturas/views", Facturas, name="facturas")
]