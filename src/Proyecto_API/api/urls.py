from django.urls import path
from .views import *

app_main = "main"

urlpatterns=[
    # URLs Productos
    path('articulos/', ArticuloView.as_view(), name='articulo_list'),
    path('articulos/<int:id>', ArticuloView.as_view(), name='articulo_process'),
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
    path("home/views", Home, name="home"),
    path("articulos/views", Products, name="articulos"),
    path("articulos/add_item", Add_Item, name="facturas"),
    path("facturas/views", Facturas, name="facturas"),
    path("facturas/add_factura", Add_Factura)
]