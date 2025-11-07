from django.db import models
# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100, unique=True)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_empresa
        
# ==========================================
# MODELO: PRODUCTO (Actualizado para usar Proveedor)
# ==========================================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    # Relacionado con Proveedor (antes era Categoria)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="productos") 
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    fecha_agregado = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    imagen = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"