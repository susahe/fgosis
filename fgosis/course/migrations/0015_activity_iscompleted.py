# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20160222_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='iscompleted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]