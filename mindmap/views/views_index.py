#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_index.py
DATE: 17-7-27 下午12:28
DESC: 
"""
from django.shortcuts import render

from mindmap.models import Category, MindMap


def index(request):
    context = {
        'title': 'MindShare',
        'categoryFirst': Category.objects.filter(parent__isnull=True),
        'items': MindMap.objects.all().order_by('-create_date'),
    }

    return render(request, 'mindmap/index.html', context=context)
