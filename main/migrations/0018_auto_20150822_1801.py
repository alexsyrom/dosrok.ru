# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150822_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='is_opened',
            new_name='state',
        ),
    ]
