from django.contrib import admin
from .models import Medicamento, Proveedor, Entrada, Salida

# Registro de modelos en el panel de administración
admin.site.register(Medicamento)
admin.site.register(Proveedor)
admin.site.register(Entrada)
admin.site.register(Salida)
