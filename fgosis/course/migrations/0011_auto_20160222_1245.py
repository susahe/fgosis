# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20160209_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
