# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150807_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='test_mark',
            field=models.PositiveIntegerField(default=0, verbose_name='Семестровая контрольная'),
        ),
    ]
