# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20160130_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='like',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
