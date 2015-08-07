# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150807_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('is_opened', models.BooleanField(default=True, verbose_name='Конкурс открыт')),
                ('rules', models.TextField(default='', verbose_name='Правила конкурса')),
                ('date', models.DateField(null=True, verbose_name='Дата проведения досрочного экзамена', blank=True)),
                ('place', models.CharField(max_length=100, default='', verbose_name='Место проведения досрочного экзамена')),
                ('program', models.FileField(null=True, verbose_name='Экзаменационная программа', blank=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Main',
        ),
    ]
