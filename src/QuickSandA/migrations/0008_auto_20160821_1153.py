# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickSandA', '0007_auto_20160821_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='other_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meetup_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]