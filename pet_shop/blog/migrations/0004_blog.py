# Generated by Django 3.2.18 on 2023-05-20 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300, verbose_name='Titulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen', models.ImageField(upload_to='blog/images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'db_table': 'blog',
                'managed': True,
            },
        ),
    ]
