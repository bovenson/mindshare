# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindmap', '0006_auto_20170728_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mindmap',
            name='category',
        ),
        migrations.AddField(
            model_name='mindmap',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mindmap.Category'),
        ),
    ]
