# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160530_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]