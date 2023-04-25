
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Medicamento, Proveedor, Entrada, Salida
from .forms import MedicamentoForm, ProveedorForm, EntradaForm, SalidaForm
from django.shortcuts import render

def listado_medicamentos(request):
    return render(request, 'listado_medicamentos.html')
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'stockmedicamentos/stock/lista_medicamentos.html', {'medicamentos': medicamentos})

def detalle_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    return render(request, 'stock/detalle_medicamento.html', {'medicamento': medicamento})

def nuevo_medicamento(request):
    if request.method == "POST":
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            medicamento = form.save(commit=False)
            medicamento.save()
            return redirect('detalle_medicamento', pk=medicamento.pk)
    else:
        form = MedicamentoForm()
    return render(request, 'stock/editar_medicamento.html', {'form': form})

def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == "POST":
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            medicamento = form.save(commit=False)
            medicamento.save()
            return redirect('detalle_medicamento', pk=medicamento.pk)
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'stock/editar_medicamento.html', {'form': form})

def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    medicamento.delete()
    return redirect('lista_medicamentos')

# Las vistas para Proveedor, Entrada y Salida serían similares

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def nuevo_proveedor(request):
    return render(request, 'nuevo_proveedor.html')

def detalle_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def editar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})
def detalle_entrada(request, pk):
    return render(request, 'detalle_entrada.html')

def lista_salidas(request):
    return render(request, 'lista_salidas.html')

def nueva_salida(request):
    return render(request, 'nueva_salida.html')

def detalle_salida(request, pk):
    return render(request, 'detalle_salida.html')

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'stock/lista_entradas.html', {'entradas': entradas})

def detalle_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'stock/detalle_entrada.html', {'entrada': entrada})

def nueva_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save()
            messages.success(request, 'Entrada creada correctamente.')
            return redirect('detalle_entrada', pk=entrada.pk)
    else:
        form = EntradaForm()
    return render(request, 'stock/editar_entrada.html', {'form': form})

def editar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            entrada = form.save()
            messages.success(request, 'Entrada actualizada correctamente.')
            return redirect('detalle_entrada', pk=entrada.pk)
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'stock/editar_entrada.html', {'form': form})