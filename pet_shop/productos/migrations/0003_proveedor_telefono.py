# Generated by Django 3.2.18 on 2023-05-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, verbose_name='Telefono'),
        ),
    ]