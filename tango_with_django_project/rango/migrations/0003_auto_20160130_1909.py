# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_likes_ox_views'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='likes',
            new_name='Like',
        ),
        migrations.RenameModel(
            old_name='views',
            new_name='View',
        ),
    ]
