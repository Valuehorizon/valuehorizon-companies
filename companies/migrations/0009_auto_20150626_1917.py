# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_person_nationality'),
        ('companies', '0008_auto_20150622_1424'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Executives',
            new_name='Executive',
        ),
    ]
