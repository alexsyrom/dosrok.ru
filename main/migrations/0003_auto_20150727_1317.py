# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150727_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(verbose_name='Группа', blank=True, max_length=6),
        ),
    ]
