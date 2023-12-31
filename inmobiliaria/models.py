from django.db import models

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    area = models.FloatField()  # Puedes ajustar el tipo de campo según tus necesidades
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
    foto_portada = models.ImageField(upload_to='inmuebles/')  
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

