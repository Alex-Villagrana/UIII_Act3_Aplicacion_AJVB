# Contenido de app_Skateshop/admin.py (ACTUALIZADO)
from django.contrib import admin
from .models import Cliente, Producto, Proveedor # Importar los 3 modelos

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'activo')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'contacto', 'telefono', 'activo')
    search_fields = ('nombre_empresa',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'proveedor', 'disponible')
    list_filter = ('disponible', 'proveedor')
    search_fields = ('nombre', 'marca')