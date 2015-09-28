# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_remove_company_is_listed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='director',
            name='special_category',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='special_category',
        ),
        migrations.AlterField(
            model_name='company',
            name='financial_publication_frequency',
            field=models.CharField(default=b'U', help_text=b'How often does this company produce financial statements?', max_length=1, choices=[('A', 'Annual'), ('S', 'Semi-Annual'), ('Q', 'Quarterly'), ('U', 'Unknown')]),
        ),
        migrations.AlterField(
            model_name='industry',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by user (or otherwise customized)'),
        ),
        migrations.AlterField(
            model_name='industrygroup',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by user (or otherwise customized)'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by user (or otherwise customized)'),
        ),
        migrations.AlterField(
            model_name='subindustry',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by user (or otherwise customized)'),
        ),
    ]
