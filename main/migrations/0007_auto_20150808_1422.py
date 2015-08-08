# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150808_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='test_mark',
            field=models.PositiveIntegerField(verbose_name='Семестровая', default=0),
        ),
    ]
