# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindmap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ManyToManyField(to='mindmap.Category'),
        ),
    ]