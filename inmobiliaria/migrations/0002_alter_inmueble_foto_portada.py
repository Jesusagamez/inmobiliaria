# Generated by Django 5.0 on 2023-12-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='foto_portada',
            field=models.ImageField(upload_to='media/inmuebles/'),
        ),
    ]