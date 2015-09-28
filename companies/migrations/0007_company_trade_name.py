# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20150617_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='trade_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
