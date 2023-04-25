from django import forms
from .models import Medicamento, Proveedor, Entrada, Salida

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ('nombre', 'proveedor', 'cantidad', 'fecha_vencimiento')

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre', 'direccion', 'telefono')

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('medicamento', 'cantidad', 'fecha')

class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ('medicamento', 'cantidad', 'fecha')
