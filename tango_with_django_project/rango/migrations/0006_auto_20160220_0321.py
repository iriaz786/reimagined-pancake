# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20160220_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(max_length=255),
        ),
    ]
