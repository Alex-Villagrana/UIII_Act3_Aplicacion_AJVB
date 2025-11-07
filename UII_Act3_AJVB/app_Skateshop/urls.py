# Contenido de app_Skateshop/urls.py (ACTUALIZADO)
from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio_skateshop, name='inicio_skateshop'),
    
    # Rutas CRUD de Clientes
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/actualizar_post/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
    
    # Rutas futuras para Producto y Proveedor (solo placeholders)
    # path('producto/...', views.alguna_funcion_producto, name='...'),
    # path('proveedor/...', views.alguna_funcion_proveedor, name='...'),
]