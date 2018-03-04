# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField()),
                ('usuario', models.OneToOneField(related_name='perfilAlumno', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('materno', models.CharField(max_length=50)),
                ('ci', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('usuario', models.OneToOneField(related_name='perfilDirector', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('materno', models.CharField(max_length=50)),
                ('ci', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('usuario', models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_producto', models.CharField(unique=True, max_length=150)),
                ('Descripcion', models.TextField()),
                ('Precio_Venta', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('Imagen', models.FileField(null=True, upload_to=b'imagenes', blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
