# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150506_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='book_value',
        ),
        migrations.RemoveField(
            model_name='company',
            name='latest_statement_date',
        ),
        migrations.RemoveField(
            model_name='company',
            name='net_income',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_articles',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_children',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_deals',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_employees',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_financial_statements',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_key_people',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_listed_competitors',
        ),
        migrations.RemoveField(
            model_name='company',
            name='num_parents',
        ),
        migrations.RemoveField(
            model_name='company',
            name='operating_income',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_stock_exchange_symbol',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_stock_symbol',
        ),
        migrations.RemoveField(
            model_name='company',
            name='primary_stock_url',
        ),
        migrations.RemoveField(
            model_name='company',
            name='revenue',
        ),
        migrations.RemoveField(
            model_name='company',
            name='total_assets',
        ),
        migrations.RemoveField(
            model_name='company',
            name='total_cash',
        ),
        migrations.RemoveField(
            model_name='company',
            name='total_debt',
        ),
        migrations.RemoveField(
            model_name='company',
            name='total_equity',
        ),
        migrations.AlterField(
            model_name='company',
            name='is_government_agency',
            field=models.BooleanField(default=False, help_text=b'Is this company a govermenet agency?'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by Valuehorizon (or otherwise customized)'),
        ),
        migrations.AlterField(
            model_name='industrygroup',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by Valuehorizon (or otherwise customized)'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by Valuehorizon (or otherwise customized)'),
        ),
        migrations.AlterField(
            model_name='subindustry',
            name='custom',
            field=models.BooleanField(default=False, help_text=b'True if created by Valuehorizon (or otherwise customized)'),
        ),
    ]
