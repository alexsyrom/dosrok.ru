# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150809_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='PRS',
            field=models.PositiveIntegerField(verbose_name='БРС', blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='test_mark',
            field=models.PositiveIntegerField(verbose_name='Семестровая', blank=True, default=0),
        ),
    ]
