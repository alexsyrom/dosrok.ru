# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150808_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='solved_problems',
            field=models.ManyToManyField(blank=True, verbose_name='Решённые задачи', to='main.Problem'),
        ),
    ]
