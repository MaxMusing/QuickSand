# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickSandA', '0006_auto_20160821_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
    ]
