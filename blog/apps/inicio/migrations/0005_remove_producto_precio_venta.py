# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_auto_20180308_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Precio_Venta',
        ),
    ]
