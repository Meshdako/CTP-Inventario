from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    comuna = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.calle}, {self.numero}, {self.comuna}"

class Proveedor(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    giro = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    telefono = models.PositiveIntegerField()
    celular = models.PositiveIntegerField()
    web = models.URLField(max_length=200)
    ubicacion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

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
    
    def __str__(self):
        return str(self.fecha_compra)

class Categoria(models.Model):
    TIPO_CATEGORIA = [
        (1, "Mobiliario"),
        (2, "Aseo"),
        (3, "Quimica"),
        (4, "Accesorio de Computadora")
    ]
    tipo_categoria = models.PositiveIntegerField(choices=TIPO_CATEGORIA)

    def __str__(self):
        return self.get_tipo_categoria_display()

class Articulo(models.Model):
    codigo = models.CharField(max_length=5, blank=True)
    nombre_articulo = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    factura_detalle = models.ForeignKey(Factura, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def generar_codigo(self):
        if not self.codigo:
            categoria = self.categoria
            if categoria:
                # Obtener el tipo de categoría
                tipo_categoria = categoria.get_tipo_categoria_display()
                
                # Generar el código basado en el tipo de categoría
                codigo = tipo_categoria[0].upper() + str(Articulo.objects.count() + 1).zfill(4)
                self.codigo = codigo

    def save(self, *args, **kwargs):
        self.generar_codigo()  # Generar el código antes de guardar el objeto
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo

class Registro_Solicitud(models.Model):
    fecha = models.DateTimeField()
    nro_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha
    
class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=10)
    # Otros campos que desees registrar