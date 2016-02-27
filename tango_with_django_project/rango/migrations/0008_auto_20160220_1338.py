# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20160220_0406'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageAdmin',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
