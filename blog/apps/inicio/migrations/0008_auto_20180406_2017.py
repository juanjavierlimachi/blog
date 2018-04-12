# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20180406_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='enlace_url',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
