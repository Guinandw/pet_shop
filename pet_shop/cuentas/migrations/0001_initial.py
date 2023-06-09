# Generated by Django 3.2.18 on 2023-05-11 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('dni', models.IntegerField(max_length=10, unique=True)),
                ('cuit', models.IntegerField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='DNI')),
                ('alta', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('dni', models.IntegerField(max_length=10, unique=True)),
                ('cuit', models.IntegerField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='DNI')),
                ('alta', models.BooleanField(default=True, verbose_name='Activo')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('cargo', models.CharField(max_length=150, verbose_name='Cargo')),
                ('sueldo', models.IntegerField(verbose_name='Sueldo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50, verbose_name='Alias')),
                ('calle', models.CharField(max_length=100, verbose_name='Direccion Exacta')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('cp', models.IntegerField(max_length=4, verbose_name='Codigo Postal')),
                ('telefono', models.IntegerField(max_length=15, verbose_name='Telefono')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.clientes')),
            ],
            options={
                'verbose_name': 'Direccion Cliente',
                'verbose_name_plural': 'Direcciones Clientes',
                'db_table': 'direccion_cliente',
                'managed': True,
            },
        ),
    ]
