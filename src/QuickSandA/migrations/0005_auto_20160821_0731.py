# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickSandA', '0004_auto_20160821_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lactose_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nut_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
