# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Cast', models.CharField(max_length=250)),
                ('Director', models.CharField(max_length=250)),
                ('Genre', models.CharField(max_length=250)),
                ('Year', models.CharField(max_length=250)),
            ],
        ),
    ]
