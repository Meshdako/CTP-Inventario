from django.db.models.signals import pre_save, post_save
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .models import *
from .forms import *
import json

# Create your views here.

@receiver(pre_save, sender=Articulo)
def pre_save_handler(sender, instance, **kwargs):
    if instance.pk is None:
        change_type = 'Nuevo artículo'
    else:
        try:
            old_instance = Articulo.objects.get(pk=instance.pk)
        except Articulo.DoesNotExist:
            return
        if instance.cantidad > old_instance.cantidad:
            change_type = 'Aumento'
        elif instance.cantidad < old_instance.cantidad:
            change_type = 'Reducción'
        else:
            return
    log_entry = LogEntry(item=instance, change_type=change_type)
    log_entry.save()

@receiver(post_save, sender=Articulo)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        return
    try:
        old_instance = Articulo.objects.get(pk=instance.pk)
    except Articulo.DoesNotExist:
        return
    if instance.cantidad == old_instance.cantidad:
        return
    change_type = 'Aumento' if instance.cantidad > old_instance.cantidad else 'Reducción'
    log_entry = LogEntry(item=instance, change_type=change_type)
    log_entry.save()

def logs_view(request):
    logs = LogEntry.objects.all().order_by('-timestamp')
    return render(request, 'main/registros.html', {'logs': logs})

def Home(request):
    return render(request = request, template_name="main/index.html")

def Ingresos(request):
    articulos = Articulo.objects.all()
    
    if request.method == 'POST':
        articulo_id = request.POST['articulo']
        cantidad_adicional = request.POST['cantidad']
        
        # Obtén el objeto Articulo seleccionado
        articulo = Articulo.objects.get(id=articulo_id)
        
        # Aumenta la cantidad existente
        articulo.cantidad += int(cantidad_adicional)
        articulo.save()

        # Redirecciona a la página deseada después de agregar la cantidad
        return redirect('registros')
    return render(request=request, template_name="main/ingresos.html", context={'articulos': articulos})

def Egresos(request):
    articulos = Articulo.objects.all()
    
    if request.method == 'POST':
        articulo_id = request.POST['articulo']
        cantidad_adicional = request.POST['cantidad']
        
        # Obtén el objeto Articulo seleccionado
        articulo = Articulo.objects.get(id=articulo_id)
        
        # Aumenta la cantidad existente
        articulo.cantidad -= int(cantidad_adicional)
        articulo.save()

        # Redirecciona a la página deseada después de agregar la cantidad
        return redirect('registros')
    return render(request=request, template_name="main/egresos.html", context={'articulos': articulos})

def Facturas(request):
    facturas = Factura.objects.all()
    return render(request = request, template_name="main/facturas.html", context={'facturas':facturas})

def Products(request):
    articulos = Articulo.objects.all()
    return render(request = request, template_name="main/articulos.html", context={'articulos':articulos})

def crear_articulo(request):
    # Formulario
    articulo_form = ArticuloForm()

    if request.method == 'POST':
        articulo_form = ArticuloForm(request.POST)
        
        if articulo_form.is_valid():
            # Obtener los datos de los formularios
            categoria_id = request.POST.get('categoria')
            articulo_categoria = Categoria.objects.get(id=categoria_id) 


            articulo_nombre_articulo = articulo_form.cleaned_data['nombre_articulo']
            articulo_cantidad = articulo_form.cleaned_data['cantidad']
            articulo_precio_unitario = articulo_form.cleaned_data['precio_unitario']
            articulo_total = articulo_form.cleaned_data['total']

            factura_detalle_id = request.POST.get('factura_detalle')
            articulo_factura_detalle = Factura.objects.get(id=factura_detalle_id)
            
            articulo = Articulo.objects.create(
                categoria = articulo_categoria,
                nombre_articulo = articulo_nombre_articulo,
                cantidad = articulo_cantidad,
                precio_unitario = articulo_precio_unitario,
                total = articulo_total,
                factura_detalle = articulo_factura_detalle
            )
            return redirect('articulos')
        
    return render(request, 'main/add_articulo.html', {
        'articulo_form': articulo_form,
    })

def crear_factura(request):
    # Formulario
    factura_form = FacturaForm()

    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        
        if factura_form.is_valid():
            # Obtener los datos de los formularios
            factura_fecha_compra = factura_form.cleaned_data['fecha_compra']
            factura_valor_neto = factura_form.cleaned_data['valor_neto']
            factura_iva = factura_form.cleaned_data['iva']
            factura_total = factura_form.cleaned_data['total']
            factura_archivo = request.FILES['archivo']
            
            proveedor_id = request.POST.get('proveedor')  # Obtener el ID del proveedor seleccionado del formulario
            proveedor = Proveedor.objects.get(id=proveedor_id)  # Obtener la instancia del proveedor
            
            factura = Factura.objects.create(
                fecha_compra=factura_fecha_compra,
                valor_neto=factura_valor_neto,
                iva=factura_iva,
                total=factura_total,
                archivo=factura_archivo,
                proveedor=proveedor)  # Asignar el proveedor a la factura
            
            return redirect('facturas')

    return render(request, 'main/add_factura.html', {
        'factura_form': factura_form,
    })

def crear_proveedor(request):
    # Formulario
    proveedor_form = ProveedorForm()

    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        
        if proveedor_form.is_valid():
            # Obtener los datos del formulario
            rut = proveedor_form.cleaned_data['rut']
            nombre = proveedor_form.cleaned_data['nombre']
            giro = proveedor_form.cleaned_data['giro']
            correo = proveedor_form.cleaned_data['correo']
            telefono = proveedor_form.cleaned_data['telefono']
            celular = proveedor_form.cleaned_data['celular']
            web = proveedor_form.cleaned_data['web']
            ubicacion_id = request.POST.get('ubicacion')  # Obtener el ID de la ubicación seleccionada del formulario
            ubicacion = Direccion.objects.get(id=ubicacion_id)  # Obtener la instancia de la ubicación
            
            proveedor = Proveedor.objects.create(
                rut=rut,
                nombre=nombre,
                giro=giro,
                correo=correo,
                telefono=telefono,
                celular=celular,
                web=web,
                ubicacion=ubicacion
            )  # Crear una nueva instancia de Proveedor
            
            return redirect('crear_factura')

    return render(request, 'main/add_proveedor.html', {
        'proveedor_form': proveedor_form,
    })



class ArticuloView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            articulos = list(Articulo.objects.filter(id=id).values())
            if len(articulos) > 0:
                articulo = articulos[0]
                datos={'message':"Success", 'articulo':articulo}
            else:
                datos={'message':"Articulo no encontrado..."}
            return JsonResponse(datos)
        else:
            articulos = list(Articulo.objects.values())
            if len(articulos) > 0:
                datos={'message':'Success', 'articulos':articulos}
            else:
                datos={'message':"Articulos no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        
        Articulo.objects.create(prod_nombre=jd['prod_nombre'], cant=jd['cant'], precio_unit=jd['precio_unit'], total=jd['total'], factura_detalle_id=jd['factura_detalle_id'])
        
        datos={'message':'Success'}
        # print(jd)
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        articulos = list(Articulo.objects.filter(id=id).values())
        if len(articulos) > 0:
            articulo = Articulo.objects.get(id=id)
            articulo.prod_nombre=jd['prod_nombre']
            articulo.cant=jd['cant']
            articulo.precio_unit=jd['precio_unit']
            articulo.total = jd['cant'] * jd['precio_unit']
            articulo.factura_detalle_id=jd['factura_detalle_id']
            articulo.save()
            datos = {'message': 'Success'}
        else:
            datos={'message':"Articulo no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        articulos = list(Articulo.objects.filter(id=id).values())
        if len(articulos) > 0:
            Articulo.objects.filter(id=id).delete(),
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Articulo no encontrado..."}
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