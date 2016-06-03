# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]