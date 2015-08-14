# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20150814_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=6, verbose_name='Группа', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия', null=True),
        ),
    ]
