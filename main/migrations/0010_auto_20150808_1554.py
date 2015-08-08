# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150808_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='place',
            field=models.CharField(blank=True, max_length=100, default='', verbose_name='Место проведения досрочного экзамена'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='rules',
            field=models.TextField(blank=True, default='', verbose_name='Правила конкурса'),
        ),
    ]
