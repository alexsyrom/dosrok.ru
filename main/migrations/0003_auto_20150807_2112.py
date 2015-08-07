# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150729_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='is_comment_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_end_date_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_number_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_rating_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_solution_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_state_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_statement_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_student_num_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_title_hidden',
            field=models.BooleanField(verbose_name='Скрыто', default=False),
        ),
    ]
