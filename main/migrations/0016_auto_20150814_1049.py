# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150814_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=50, default='', blank=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=6, default='', blank=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=50, default='', blank=True, verbose_name='Фамилия'),
        ),
    ]
