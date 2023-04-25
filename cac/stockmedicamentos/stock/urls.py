from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_medicamentos, name='inicio'),
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/nuevo/', views.nuevo_medicamento, name='nuevo_medicamento'),
    path('medicamentos/<int:pk>/', views.detalle_medicamento, name='detalle_medicamento'),
    path('medicamentos/<int:pk>/editar/', views.editar_medicamento, name='editar_medicamento'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedores/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/<int:pk>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/nueva/', views.nueva_entrada, name='nueva_entrada'),
    path('entradas/<int:pk>/', views.detalle_entrada, name='detalle_entrada'),
    path('salidas/', views.lista_salidas, name='lista_salidas'),
    path('salidas/nueva/', views.nueva_salida, name='nueva_salida'),
    path('salidas/<int:pk>/', views.detalle_salida, name='detalle_salida'),
]
