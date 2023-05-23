from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    comuna = models.CharField(max_length=50)

class Proveedor(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    giro = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    telefono = models.PositiveIntegerField()
    celular = models.PositiveIntegerField()
    web = models.URLField(max_length=200)
    ubicacion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def clean(self):
        if isinstance(self.rut, str):
            self.rut = self.rut.replace('.', '').replace('-', '')  # Eliminar puntos y guión
            self.rut = self.rut[:-1] + '-' + self.rut[-1]  # Agregar guión antes del dígito verificador
            self.rut = self.rut.upper()  # Convertir a mayúsculas (opcional)
        else:
            raise ValidationError('RUT inválido')

        rut_numero, rut_digito = self.rut.split('-')  # Separar número y dígito verificador

        # Validar longitud y formato del número y dígito verificador
        if not rut_numero.isdigit() or not rut_digito.isdigit() or len(rut_digito) > 1:
            raise ValidationError('RUT inválido')
    
    def save(self, *args, **kwargs):
        try:
            self.full_clean()
        except ValidationError as e:
            raise e
        else:
            super().save(*args, **kwargs)

class Factura(models.Model):
    fecha_compra = models.DateField()
    valor_neto = models.PositiveIntegerField()
    iva = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='documentos/%Y/%m/%d/', default='default.pdf')

class Categoria(models.Model):
    TIPO_CATEGORIA = [
        (1, "Mobiliario"),
        (2, "Aseo"),
        (3, "Quimica"),
        (4, "Accesorio de Computadora")
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