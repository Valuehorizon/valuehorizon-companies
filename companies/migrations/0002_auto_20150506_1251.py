# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('people', '0001_initial'),
        ('countries', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='executives',
            name='person',
            field=models.ForeignKey(to='people.Person'),
        ),
        migrations.AddField(
            model_name='directors',
            name='company',
            field=models.ForeignKey(to='companies.Company'),
        ),
        migrations.AddField(
            model_name='directors',
            name='person',
            field=models.ForeignKey(to='people.Person'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(to='countries.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(blank=True, editable=False, to='companies.Industry', null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='industry_group',
            field=models.ForeignKey(blank=True, editable=False, to='companies.IndustryGroup', null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(blank=True, editable=False, to='companies.Sector', null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sub_industry',
            field=models.ForeignKey(to='companies.SubIndustry'),
        ),
        migrations.AlterUniqueTogether(
            name='ownership',
            unique_together=set([('parent', 'child')]),
        ),
        migrations.AlterUniqueTogether(
            name='directors',
            unique_together=set([('company', 'person', 'start_date', 'end_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together=set([('name', 'country')]),
        ),
    ]
