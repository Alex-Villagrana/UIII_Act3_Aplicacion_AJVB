# Contenido de app_Skateshop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto, Proveedor # Importamos los modelos

# 1. Función de Inicio
def inicio_skateshop(request):
    return render(request, 'inicio.html')

# 2. CRUD: Agregar Cliente
def agregar_cliente(request):
    if request.method == 'POST':
        # No validar entrada de datos:
        cliente = Cliente(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            activo=request.POST.get('activo', False) == 'on'
        )
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

# 3. CRUD: Ver Clientes (Listado)
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido')
    context = {'clientes': clientes}
    return render(request, 'cliente/ver_clientes.html', context)

# 4. CRUD: Actualizar Cliente (Mostrar Formulario)
def actualizar_cliente(request, pk):
    cliente_a_actualizar = get_object_or_404(Cliente, pk=pk)
    context = {'cliente': cliente_a_actualizar}
    return render(request, 'cliente/actualizar_cliente.html', context)

# 5. CRUD: Actualizar Cliente (Procesar POST)
def realizar_actualizacion_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.activo = request.POST.get('activo', False) == 'on'
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', pk=pk)

# 6. CRUD: Borrar Cliente
def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    context = {'cliente': cliente}
    return render(request, 'cliente/borrar_cliente.html', context)