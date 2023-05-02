from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json

# Create your views here.

def Home(request):
    user_count = User.objects.count()
    model1_data = Producto.objects.all()
    model2_data = Factura.objects.all()
    context = {
        'user_count': user_count,
        'model1_data': model1_data,
        'model2_data': model2_data,
    }
    return render(request, 'main/index.html', context)

def Facturas(request):
    facturas = Factura.objects.all()
    return render(request = request, template_name="main/facturas.html", context={'facturas':facturas})

def Products(request):
    productos = Producto.objects.all()
    return render(request = request, template_name="main/products.html", context={'productos':productos})

def Add_Item(request):
    facturas = Factura.objects.all()
    return render(request = request, template_name="main/add_item.html", context={'facturas':facturas})


class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            productos = list(Producto.objects.filter(id=id).values())
            if len(productos) > 0:
                producto = productos[0]
                datos={'message':"Success", 'producto':producto}
            else:
                datos={'message':"Producto no encontrado..."}
            return JsonResponse(datos)
        else:
            productos=list(Producto.objects.values())
            if len(productos) > 0:
                datos={'message':'Success', 'productos':productos}
            else:
                datos={'message':"Productos no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        Producto.objects.create(prod_nombre=jd['prod_nombre'], cant=jd['cant'], precio_unit=jd['precio_unit'], total=jd['total'], factura_detalle_id=jd['factura_detalle_id'])
        datos={'message':'Success'}
        # print(jd)
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        productos = list(Producto.objects.filter(id=id).values())
        if len(productos) > 0:
            producto = Producto.objects.get(id=id)
            producto.prod_nombre=jd['prod_nombre']
            producto.cant=jd['cant']
            producto.precio_unit=jd['precio_unit']
            producto.total = jd['cant'] * jd['precio_unit']
            producto.factura_detalle_id=jd['factura_detalle_id']
            producto.save()
            datos = {'message': 'Success'}
        else:
            datos={'message':"Producto no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        producto = list(Producto.objects.filter(id=id).values())
        if len(producto) > 0:
            Producto.objects.filter(id=id).delete(),
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Producto no encontrado..."}
        return JsonResponse(datos)

class FacturaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            facturas = list(Factura.objects.filter(id=id).values())
            if len(facturas) > 0:
                factura = facturas[0]
                datos={'message':"Success", 'factura':factura}
            else:
                datos={'message':"Factura no encontrada..."}
            return JsonResponse(datos)
        else:
            facturas=list(Factura.objects.values())
            if len(facturas) > 0:
                datos={'message':'Success', 'facturas':facturas}
            else:
                datos={'message':"Facturas no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request, id):
        jd = json.loads(request.body)
        factura = list(Factura.objects.filter(id=id).values())
        if len(factura) > 0:
            factura = Factura.objects.get(id=id)
            factura.fecha_compra=jd['fecha_compra']
            factura.valor_neto=jd['valor_neto']
            factura.iva=jd['iva']
            factura.total=jd['total']
            factura.id_proveedor_id=jd['id_proveedor_id']
            factura.save()
            datos = {'message': 'Success'}
        else:
            datos={'message':"Factura no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        factura = list(Factura.objects.filter(id=id).values())
        if len(factura) > 0:
            Factura.objects.filter(id=id).delete(),
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Factura no encontrada..."}
        return JsonResponse(datos)

class ProveedorView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            proveedores = list(Proveedor.objects.filter(id=id).values())
            if len(proveedores) > 0:
                proveedor = proveedores[0]
                datos={'message':"Success", 'proveedor':proveedor}
            else:
                datos={'message':"Proveedor no encontrado..."}
            return JsonResponse(datos)
        else:
            proveedores=list(Proveedor.objects.values())
            if len(proveedores) > 0:
                datos={'message':'Success', 'proveedores':proveedores}
            else:
                datos={'message':"Proveedores no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request, id):
        jd = json.loads(request.body)
        proveedor = list(Proveedor.objects.filter(id=id).values())
        if len(proveedor) > 0:
            proveedor = Proveedor.objects.get(id=id)
            proveedor.rut=jd['rut']
            proveedor.nombre=jd['nombre']
            proveedor.giro=jd['giro']
            proveedor.direcc=jd['direcc']
            proveedor.telefono=jd['telefono']
            proveedor.save()
            datos = {'message': 'Success'}
        else:
            datos={'message':"Proveedor no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        proveedor = list(Proveedor.objects.filter(id=id).values())
        if len(proveedor) > 0:
            Proveedor.objects.filter(id=id).delete(),
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Proveedor no encontrado..."}
        return JsonResponse(datos)
    
class RegistroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            registros = list(Registro_Solicitud.objects.filter(id=id).values())
            if len(registros) > 0:
                registro = registros[0]
                datos={'message':"Success", 'registro':registro}
            else:
                datos={'message':"Registro no encontrado..."}
            return JsonResponse(datos)
        else:
            registros=list(Registro_Solicitud.objects.values())
            if len(registros) > 0:
                datos={'message':'Success', 'registros':registros}
            else:
                datos={'message':"Registros no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request, id):
        jd = json.loads(request.body)
        registro = list(Registro_Solicitud.objects.filter(id=id).values())
        if len(registro) > 0:
            registro = Registro_Solicitud.objects.get(id=id)
            registro.rut=jd['rut']
            registro.nombre=jd['nombre']
            registro.save()
            datos = {'message': 'Success'}
        else:
            datos={'message':"Registro no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        registro = list(Registro_Solicitud.objects.filter(id=id).values())
        if len(registro) > 0:
            Registro_Solicitud.objects.filter(id=id).delete(),
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Registro no encontrado..."}
        return JsonResponse(datos)