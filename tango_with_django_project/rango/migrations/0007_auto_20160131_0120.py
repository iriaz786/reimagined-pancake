# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20160131_0041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='likes',
        ),
    ]
