# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_type', models.CharField(max_length=255, choices=[('LTD', 'Limited Liability'), ('P', 'Partnership'), ('SP', 'Sole Proprietorship'), ('NV', 'Naamloze vennootschap')])),
                ('status_type', models.CharField(max_length=1, choices=[('A', 'Active (Going Concern)'), ('N', 'Active (Non-Going Concern)'), ('D', 'Active (Developmental)'), ('I', 'Inactive'), ('U', 'Unknown')])),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=15, null=True, blank=True)),
                ('previous_name', models.CharField(help_text=b'Previous name, if any', max_length=255, null=True, blank=True)),
                ('include_article_in_description', models.BooleanField(default=False, help_text=b'eg. [the] Petroleum company of Trinidad')),
                ('slug_name', models.CharField(unique=True, max_length=255)),
                ('registration_date', models.DateField(help_text=b'Date founded', null=True, blank=True)),
                ('address', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('short_description', models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(370)])),
                ('phone', models.CharField(max_length=255, blank=True)),
                ('fax', models.CharField(max_length=255, blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('sub_industry_name', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('industry_name', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('industry_group_name', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('sector_name', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('financial_year_end', models.DateField(null=True, blank=True)),
                ('financial_publication_frequency', models.CharField(default=b'U', max_length=1, choices=[('A', 'Annual'), ('S', 'Semi-Annual'), ('Q', 'Quarterly'), ('U', 'Unknown')])),
                ('is_auditor', models.BooleanField(default=False, help_text=b'Is this company an Auditor, eg. PwC, Deloitte, etc.?.')),
                ('is_credit_rating_agency', models.BooleanField(default=False, help_text=b'is this company a credit rating agency, eg. S&P, Fitch, etc.')),
                ('is_government_agency', models.BooleanField(default=False, help_text=b'Is this company a govermnet agency?')),
                ('is_listed', models.BooleanField(default=False, help_text=b'Is this company listed on a stock exchange?')),
                ('is_private', models.BooleanField(default=True, help_text=b'Is this company 100% private, i.e. no financial information available?')),
                ('is_non_profit', models.BooleanField(default=False, help_text=b'Is this a non-profit company?')),
                ('is_government', models.BooleanField(default=False, help_text=b'Is this a government?')),
                ('is_fund', models.BooleanField(default=False, help_text=b'Is this a Mutual Fund?')),
                ('latest_statement_date', models.DateField(null=True, blank=True)),
                ('revenue', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('operating_income', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('net_income', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('total_assets', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('total_cash', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('total_debt', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('total_equity', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('book_value', models.DecimalField(null=True, editable=False, max_digits=20, decimal_places=2, blank=True)),
                ('num_employees', models.IntegerField(null=True, blank=True)),
                ('num_articles', models.IntegerField(default=0, editable=False)),
                ('num_financial_statements', models.IntegerField(default=0, editable=False)),
                ('num_deals', models.IntegerField(default=0, editable=False)),
                ('num_key_people', models.IntegerField(default=0, editable=False)),
                ('num_listed_competitors', models.IntegerField(default=0, editable=False)),
                ('num_children', models.IntegerField(default=0, editable=False)),
                ('num_parents', models.IntegerField(default=0, editable=False)),
                ('primary_stock_url', models.CharField(max_length=255, null=True, blank=True)),
                ('primary_stock_symbol', models.CharField(max_length=255, null=True, blank=True)),
                ('primary_stock_exchange_symbol', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('is_current', models.BooleanField(default=True)),
                ('position', models.CharField(max_length=255, blank=True)),
                ('special_category', models.CharField(blank=True, max_length=3, null=True, choices=[('CHM', 'Chairman'), ('COS', 'Corporate Secretary')])),
            ],
            options={
                'ordering': ['is_current', 'company', 'person'],
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='Executives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('is_current', models.BooleanField(default=True)),
                ('position', models.CharField(max_length=255, blank=True)),
                ('special_category', models.CharField(blank=True, max_length=3, null=True, choices=[('CEO', 'Chief Executive Officer'), ('CFO', 'Chief Financial Officer'), ('COO', 'Chief Operating Officer')])),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
            options={
                'ordering': ['is_current', 'company', 'person'],
                'verbose_name': 'Executive',
                'verbose_name_plural': 'Executives',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(unique=True, max_length=6)),
                ('description', models.TextField(blank=True)),
                ('custom', models.BooleanField(default=False, help_text=b'True if created by Valuehorizon')),
            ],
            options={
                'ordering': ['symbol', 'name'],
                'verbose_name': 'GICS 3 Industry',
                'verbose_name_plural': 'GICS 3 Industry',
            },
        ),
        migrations.CreateModel(
            name='IndustryGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(unique=True, max_length=4)),
                ('description', models.TextField(blank=True)),
                ('custom', models.BooleanField(default=False, help_text=b'True if created by Valuehorizon')),
            ],
            options={
                'ordering': ['symbol', 'name'],
                'verbose_name': 'GICS 2 Industry Group',
                'verbose_name_plural': 'GICS 2 Industry Groups',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('ownership_type', models.CharField(max_length=3, choices=[('SUB', 'Subsidiary'), ('ASS', 'Associate'), ('JV', 'Joint Venture'), ('I', 'Institutional')])),
                ('child', models.ForeignKey(related_name='child', to='companies.Company')),
                ('parent', models.ForeignKey(related_name='parent', to='companies.Company')),
            ],
            options={
                'ordering': ['parent', 'child'],
                'verbose_name': 'Ownership',
                'verbose_name_plural': 'Ownership',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(unique=True, max_length=2)),
                ('description', models.TextField(blank=True)),
                ('custom', models.BooleanField(default=False, help_text=b'True if created by Valuehorizon')),
            ],
            options={
                'ordering': ['symbol', 'name'],
                'verbose_name': 'GICS 1 Sector',
                'verbose_name_plural': 'GICS 1 Sectors',
            },
        ),
        migrations.CreateModel(
            name='SubIndustry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(unique=True, max_length=8)),
                ('description', models.TextField(blank=True)),
                ('custom', models.BooleanField(default=False, help_text=b'True if created by Valuehorizon')),
                ('industry', models.ForeignKey(to='companies.Industry')),
            ],
            options={
                'ordering': ['symbol', 'name'],
                'verbose_name': 'GICS 4 Sub-Industry',
                'verbose_name_plural': 'GICS 4 Sub-Industry',
            },
        ),
        migrations.AddField(
            model_name='industrygroup',
            name='sector',
            field=models.ForeignKey(to='companies.Sector'),
        ),
        migrations.AddField(
            model_name='industry',
            name='industry_group',
            field=models.ForeignKey(to='companies.IndustryGroup'),
        ),
        migrations.AddField(
            model_name='industry',
            name='sector',
            field=models.ForeignKey(to='companies.Sector'),
        ),
    ]
