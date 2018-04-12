# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_auto_20180406_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='enlace_url',
            field=models.TextField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
