from django import forms

class ArticuloForm(forms.Form):
    # Proveedor
    rut = forms.IntegerField()
    # Factura
    fecha_compra = forms.DateField()
    valor_neto = forms.IntegerField()
    iva = forms.IntegerField()
    total = forms.IntegerField()
    archivo = forms.FileField()
    # Articulo
    categoria = forms.ChoiceField(choices=((1, 'Mobiliario'), (2, 'Aseo'), (3, 'Química'), (4, 'Accesorios de Computadora')))
    nombre_articulo = forms.CharField()
    cantidad = forms.IntegerField()
    precio_unitario = forms.DecimalField()
    total_articulo = forms.DecimalField()