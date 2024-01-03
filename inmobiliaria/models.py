from django.db import models


class Inmueble(models.Model):
  
    CATEGORIAS_CHOICES = [
        ('unifamiliar', 'unifamiliar'),
        ('apartamento', 'apartamento'),
        ('mansion', 'mansión'),
        ('casa de campo', 'casa de Campo'),
        ('casa de playa', 'casa de Playa'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    area = models.FloatField()  
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
    foto_portada = models.ImageField(upload_to='inmuebles/')  
    ubicacion = models.CharField(max_length=255)
    ruta_link = models.URLField(max_length=200, blank=True, null=True)
    categorias = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES, blank=True)

    def __str__(self):
        return self.nombre


