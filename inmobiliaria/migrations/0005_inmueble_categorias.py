# Generated by Django 5.0 on 2024-01-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0004_inmueble_ruta_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='categorias',
            field=models.CharField(blank=True, choices=[('unifamiliar', 'Unifamiliar'), ('apartamento', 'Apartamento'), ('mansion', 'Mansión'), ('casa_de_campo', 'Casa de Campo'), ('casa_de_playa', 'Casa de Playa')], max_length=20),
        ),
    ]
