# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickSandA', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='user_id',
            new_name='seller',
        ),
    ]
