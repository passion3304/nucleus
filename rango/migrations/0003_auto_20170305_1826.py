# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170228_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=80, verbose_name='case')),
                ('test', models.CharField(max_length=80, verbose_name='test')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='TestCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository_url', models.CharField(max_length=60, verbose_name='repository url')),
                ('date_run', models.DateTimeField(auto_now_add=True, verbose_name='date run')),
                ('test_version', models.CharField(max_length=10, verbose_name='tests version')),
                ('log', models.TextField(verbose_name='log')),
                ('time_taken', models.PositiveIntegerField(verbose_name='time taken')),
                ('status', models.CharField(max_length=15, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='TestRunDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.BooleanField(default=False, verbose_name='passed')),
                ('log', models.TextField(verbose_name='log')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rango.TestRun')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rango.Test')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rango.TestCategory'),
        ),
    ]
