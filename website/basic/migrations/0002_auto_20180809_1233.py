# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-09 12:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuser',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 9, 12, 33, 18, 55795, tzinfo=utc)),
        ),
    ]
