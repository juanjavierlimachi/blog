# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_producto_gusto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='gusto',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
