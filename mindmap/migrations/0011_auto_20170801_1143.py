# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 03:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mindmap', '0010_mindmapvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='count',
            new_name='cnt',
        ),
    ]
