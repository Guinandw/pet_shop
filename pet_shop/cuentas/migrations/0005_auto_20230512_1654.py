# Generated by Django 3.2.18 on 2023-05-12 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_auto_20230511_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Direccion',
        ),
    ]
