# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150526_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyNameChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('name_before', models.CharField(max_length=255)),
                ('name_after', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=85)),
                ('long_description', models.CharField(max_length=255)),
                ('status', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', 'Completed'), (b'FA', 'Failed'), (b'UP', 'Upcoming')])),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Company Name Change',
                'verbose_name_plural': 'Company Name Changes',
            },
        ),
    ]
