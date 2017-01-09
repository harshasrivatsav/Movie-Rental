# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='Plot',
            field=models.CharField(default='', max_length=2500),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='Poster',
            field=models.CharField(default='', max_length=2500),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='Rating',
            field=models.CharField(default='', max_length=25),
        ),
    ]
