# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='KID',
            field=models.CharField(editable=False, max_length=255, unique=True, verbose_name='ID', blank=True),
        ),
    ]
