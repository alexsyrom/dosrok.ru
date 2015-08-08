# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150808_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='example',
            options={'verbose_name': 'Пример', 'verbose_name_plural': 'Примеры'},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]
