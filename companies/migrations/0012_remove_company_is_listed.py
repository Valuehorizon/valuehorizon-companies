# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_company_latest_incorporation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='is_listed',
        ),
    ]
