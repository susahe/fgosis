# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('duration', models.IntegerField(default=0)),
                ('activity_type', models.CharField(choices=[('de', 'Demostration'), ('pr', 'Presentation'), ('ex', 'Exercise'), ('as', 'Assignment'), ('pr', 'Project'), ('db', 'Debate'), ('qu', 'Questining')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('duration', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('duration', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('duration', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers_Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_completed', models.BooleanField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('duration', models.IntegerField(default=0)),
                ('course_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseModule')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Topic'),
        ),
        migrations.AddField(
            model_name='activity',
            name='leson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Lesson'),
        ),
    ]
