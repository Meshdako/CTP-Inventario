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
    correo = models.EmailField(max_length=254)
    telefono = models.PositiveIntegerField()
    celular = models.PositiveIntegerField()
    web = models.URLField(max_length=200)
    ubicacion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class Factura(models.Model):
    fecha_compra = models.DateField()
    valor_neto = models.PositiveIntegerField()
    iva = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Categoria(models.Model):
    TIPO_CATEGORIA = [
        (1, "Mobiliario"),
        (2, "Aseo"),
        (3, "Quimica")
    ]
    tipo_categoria = models.PositiveIntegerField(choices=TIPO_CATEGORIA)

class Articulo(models.Model):
    codigo = models.PositiveIntegerField()
    nombre_articulo = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    factura_detalle = models.ForeignKey(Factura, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Registro_Solicitud(models.Model):
    fecha = models.DateTimeField()
    nro_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)