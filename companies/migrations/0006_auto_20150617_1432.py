# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_remove_company_previous_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='include_article_in_description',
            field=models.BooleanField(default=False, help_text=b'eg. [the] National Biscuit Company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='short_name',
            field=models.CharField(help_text=b'eg. Freddie Mac', max_length=15, null=True, blank=True),
        ),
    ]
