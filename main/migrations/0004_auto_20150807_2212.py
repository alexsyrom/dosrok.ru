# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150807_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('statement', models.FileField(upload_to='', verbose_name='Условие')),
                ('comment', models.FileField(blank=True, upload_to='', verbose_name='Комментарий', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('is_opened', models.BooleanField(verbose_name='Конкурс открыт', default=True)),
                ('rules', models.TextField(verbose_name='Правила конкурса', default='')),
                ('date', models.DateField(blank=True, verbose_name='Дата проведения досрочного экзамена', null=True)),
                ('place', models.CharField(max_length=100, verbose_name='Место проведения досрочного экзамена', default='')),
                ('program', models.FileField(blank=True, upload_to='', verbose_name='Экзаменационная программа', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='problem',
            name='state',
            field=models.BooleanField(verbose_name='Конкурс открыт', default=True),
        ),
    ]
