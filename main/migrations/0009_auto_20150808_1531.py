# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150808_1434'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('lastname', 'firstname', 'group')]),
        ),
    ]
