# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20160220_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
