# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-12 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mindmap', '0011_auto_20170801_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='标题')),
                ('content', models.CharField(blank=True, max_length=10000, verbose_name='内容')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]