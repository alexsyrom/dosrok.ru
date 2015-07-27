# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('statement', models.FileField(upload_to='', verbose_name='Условие')),
                ('number', models.PositiveIntegerField(verbose_name='Номер')),
                ('KID', models.CharField(max_length=10, blank=True, verbose_name='ID')),
                ('state', models.CharField(max_length=10, choices=[('OPENED', 'Конкурс открыт'), ('CLOSED', 'Конкурс закрыт')], verbose_name='Конкурсное состояние')),
                ('end_date', models.DateField(null=True, blank=True, verbose_name='Дата окончания конкурса')),
                ('student_num', models.PositiveIntegerField(default=0, verbose_name='Число студентов, решивших задачу')),
                ('rating', models.DecimalField(max_digits=9, default=Decimal('Infinity'), decimal_places=8, verbose_name='Рейтинг')),
                ('solution', models.FileField(null=True, blank=True, upload_to='', verbose_name='Решение')),
                ('comment', models.FileField(null=True, blank=True, upload_to='', verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('lastname', models.CharField(max_length=50, blank=True, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=50, blank=True, verbose_name='Имя')),
                ('group', models.PositiveIntegerField(blank=True, verbose_name='Группа')),
                ('KID', models.CharField(max_length=10, default=0, blank=True, verbose_name='ID')),
                ('rating', models.DecimalField(max_digits=11, default=Decimal('0.0'), decimal_places=8, verbose_name='Рейтинг')),
                ('is_allowed', models.BooleanField(default=False, verbose_name='Допуск')),
                ('nec_conditions', models.BooleanField(default=False, verbose_name='Необходимые условия')),
                ('recommendation', models.BooleanField(default=False, verbose_name='Рекомендация преподавателя')),
                ('PRS', models.PositiveIntegerField(default=0, verbose_name='БРС')),
                ('test_mark', models.PositiveIntegerField(default=0, verbose_name='Семестровая')),
                ('solved_problems', models.ManyToManyField(blank=True, to='main.Problem')),
            ],
        ),
    ]
