# Generated by Django 5.0 on 2023-12-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('area', models.FloatField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_alquiler', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto_portada', models.ImageField(upload_to='inmuebles/')),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
    ]