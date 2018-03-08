# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_producto_en_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='gusto',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
