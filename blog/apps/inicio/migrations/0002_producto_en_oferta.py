# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='En_oferta',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
