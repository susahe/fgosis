# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_practical_lesson_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='session',
            field=models.CharField(choices=[('t', 'Theory'), ('p', 'Practical'), ('l', 'Lab')], default='t', max_length=15),
            preserve_default=False,
        ),
    ]
