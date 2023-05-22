from django import forms

class ArticuloForm(forms.Form):
    fecha_compra = forms.DateField()
    valor_neto = forms.IntegerField()
    iva = forms.IntegerField()
    total = forms.IntegerField()
    categoria = forms.ChoiceField(choices=((1, 'Mobiliario'), (2, 'Aseo'), (3, 'Química')))
    nombre_articulo = forms.CharField()
    cantidad = forms.IntegerField()
    precio_unitario = forms.DecimalField()
    total = forms.DecimalField()