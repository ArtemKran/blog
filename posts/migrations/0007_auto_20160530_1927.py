# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='inserted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]