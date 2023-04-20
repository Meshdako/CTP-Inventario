from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.

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
                datos={'message':"Producto no encontrados..."}
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
            producto.total=jd['total']
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