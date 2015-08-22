# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150814_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='end_date',
            field=models.DateTimeField(verbose_name='Дата окончания конкурса', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='end_date',
            field=models.DateTimeField(verbose_name='Дата окончания конкурса', blank=True, null=True),
        ),
    ]
