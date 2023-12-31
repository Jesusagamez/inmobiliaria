from django.contrib import admin
from .models import Inmueble

class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area', 'precio_venta', 'precio_alquiler', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')

admin.site.register(Inmueble, InmuebleAdmin)

