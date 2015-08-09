# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150808_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='date',
            new_name='exam_date',
        ),
        migrations.AddField(
            model_name='subject',
            name='end_date',
            field=models.DateField(verbose_name='Дата окончания конкурса', null=True, blank=True),
        ),
    ]
