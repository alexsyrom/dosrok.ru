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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('statement', models.FileField(upload_to='', verbose_name='Условие')),
                ('number', models.PositiveIntegerField(verbose_name='Номер')),
                ('KID', models.CharField(blank=True, max_length=10, verbose_name='ID')),
                ('state', models.CharField(max_length=10, verbose_name='Конкурсное состояние', choices=[('OPENED', 'Конкурс открыт'), ('CLOSED', 'Конкурс закрыт')])),
                ('end_date', models.DateField(blank=True, verbose_name='Дата окончания конкурса', null=True)),
                ('student_num', models.PositiveIntegerField(verbose_name='Число студентов, решивших задачу', default=0)),
                ('rating', models.DecimalField(max_digits=9, verbose_name='Рейтинг', default=Decimal('Infinity'), decimal_places=8)),
                ('solution', models.FileField(blank=True, upload_to='', verbose_name='Решение', null=True)),
                ('comment', models.FileField(blank=True, upload_to='', verbose_name='Комментарий', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('lastname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('firstname', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('group', models.PositiveIntegerField(blank=True, verbose_name='Группа')),
                ('KID', models.CharField(blank=True, max_length=10, default=0, verbose_name='ID')),
                ('rating', models.DecimalField(max_digits=11, verbose_name='Рейтинг', default=Decimal('Infinity'), decimal_places=8)),
                ('is_allowed', models.BooleanField(verbose_name='Допуск', default=False)),
                ('nec_conditions', models.BooleanField(verbose_name='Необходимые условия', default=False)),
                ('recommendation', models.BooleanField(verbose_name='Рекомендация преподавателя', default=False)),
                ('PRS', models.PositiveIntegerField(verbose_name='БРС', default=0)),
                ('test_mark', models.PositiveIntegerField(verbose_name='Семестровая', default=0)),
                ('solved_problems', models.ManyToManyField(to='main.Problem')),
            ],
        ),
    ]
