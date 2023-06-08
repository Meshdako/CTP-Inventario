from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_main = "main"

app_name= 'api'

urlpatterns=[
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    # URLs Productos
    path('articulos/', ArticuloView.as_view(), name='articulo_list'),
    path('articulos/<int:id>', ArticuloView.as_view(), name='articulo_process'),
    # URLs Facturas
    path('facturas/', FacturaView.as_view(), name='factura_list'),
    path('facturas/<int:id>', FacturaView.as_view(), name='factura_process'),
    # URLs Proveedores
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/<int:id>', ProveedorView.as_view(), name='proveedor_process'),
    # URLs Direccion
    path('direccion/', DireccionView.as_view(), name='direccion_list'),
    path('direccion/<int:id>', DireccionView.as_view(), name='direccion_process'),
    # URLs Plantillas
    path("home", Home, name="home"),
    path("ingresos", Ingresos, name="ingresos"),
    path('egresos', Egresos, name='egresos'),
    # ARTICULOS
    path("articulos/views", Products, name="articulos"),
    path('articulos/add', crear_articulo, name='crear_articulo'),
    # FACTURAS
    path("facturas/views", Facturas, name="facturas"),
    path('facturas/add', crear_factura, name='crear_factura'),
    path('facturas/edit/<int:id>', editar_factura, name='editar_factura'),
    path('facturas/delete/<int:id>', eliminar_factura, name='eliminar_factura'),
    # DIRECCION
    path('proveedor/add', crear_proveedor, name='crear_proveedor'),
    path('direccion/add', crear_direccion, name='crear_direccion'),
    # LOGS
    path('registros', logs_view, name='registros'),
]