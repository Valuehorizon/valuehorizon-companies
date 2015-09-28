# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_auto_20150626_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='latest_incorporation_date',
            field=models.DateField(help_text=b'Incorporation date of latest incarnation', null=True, blank=True),
        ),
    ]
