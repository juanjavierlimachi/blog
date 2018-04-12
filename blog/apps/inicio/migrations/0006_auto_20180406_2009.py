# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_remove_producto_precio_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Imagen',
        ),
        migrations.AddField(
            model_name='producto',
            name='enlace_url',
            field=models.TextField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
