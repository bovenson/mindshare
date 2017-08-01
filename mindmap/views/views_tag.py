#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_tag.py
DATE: 17-8-1 上午11:23
DESC: 
"""
import traceback

from django.shortcuts import render

from mindmap.models import Tag, MindMap
from mindmap.views.url_generator import tag_url_generator
from mindmap.views.views_common import return_404_page
from mindmap.views.views_pagination import get_pages


def show_tag_page(request, tid, page=1):
    try:
        tag = Tag.objects.filter(id=tid).first()
        items = MindMap.objects.filter(tags__in=[tag]).order_by('-vote')
        print(items)

        context = {
            'title': '分类 - ' + tag.title,
            'items': items,
            'tag': tag,
            'pages': get_pages(items, cur_page=page, url_generator=tag_url_generator, tid=tid),
        }
        return render(request, 'mindmap/mind-tag.html', context)
    except Exception as e:
        print(e)
        traceback.print_exc()
    return return_404_page(request)