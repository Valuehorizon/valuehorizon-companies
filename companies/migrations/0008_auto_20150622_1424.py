# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_trade_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companynamechange',
            unique_together=set([('company', 'date')]),
        ),
    ]
