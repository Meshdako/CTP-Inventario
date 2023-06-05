from django import forms
from .models import *

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'comuna']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut', 'nombre', 'giro', 'correo', 'telefono', 'celular', 'web', 'direccion']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['fecha_compra', 'valor_neto', 'iva', 'total', 'archivo', 'proveedor']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'})  # Opcional: agregar una clase CSS al campo proveedor
        }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['categoria', 'nombre_articulo', 'cantidad', 'precio_unitario', 'total', 'factura_detalle']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'factura_detalle': forms.Select(attrs={'class': 'form-control'})  # Agregar una clase CSS al campo factura_detalle
        }
