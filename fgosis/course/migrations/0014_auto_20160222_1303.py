# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 13:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20160222_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_diary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 22, 13, 2, 47, 851540, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers_diary',
            name='tobecompleted',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 22, 13, 2, 56, 828991, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers_diary',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 22, 13, 3, 4, 359080, tzinfo=utc)),
            preserve_default=False,
        ),
    ]