from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    comuna = models.CharField(max_length=50)

class Proveedor(models.Model):
    rut = models.PositiveIntegerField()
    nombre = models.CharField(max_length=50)
    giro = models.CharField(max_length=100)
    direcc = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.PositiveIntegerField()

class Factura(models.Model):
    fecha_compra = models.DateField()
    valor_neto = models.PositiveIntegerField()
    iva = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Producto(models.Model):
    prod_nombre = models.CharField(max_length=50)
    cant = models.PositiveIntegerField()
    precio_unit = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    factura_detalle = models.ForeignKey(Factura, on_delete=models.CASCADE)

class Registro_Solicitud(models.Model):
    fecha = models.DateTimeField()
    nro_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

