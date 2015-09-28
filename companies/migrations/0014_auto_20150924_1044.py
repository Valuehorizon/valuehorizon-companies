# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_auto_20150923_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.ForeignKey(help_text=b'Country in which the company is registered', to='countries.Country'),
        ),
    ]
