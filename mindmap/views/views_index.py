#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_index.py
DATE: 17-7-27 下午12:28
DESC: 
"""
import traceback

from django.shortcuts import render

from mindmap.models import Category, MindMap
from mindmap.views.url_generator import index_url_generator
from mindmap.views.views_common import return_404_page
from mindmap.views.views_pagination import get_pages


def index(request, category=None, page=1):
    try:
        cur_category = None
        category_first = None
        category_second = None

        if category is not None:
            cur_category = Category.objects.filter(id=category).first()
            items = (MindMap.objects.filter(category_id=category, public=True) |
                     MindMap.objects.filter(category__parent=category, public=True))
        else:
            items = MindMap.objects.filter(public=True)

        # 排序
        order = request.GET.get('ord')
        if order is None or order == 'hot':
            order = 'hot'
            items = items.order_by('-vote', '-create_date')
        elif order == 'new':
            items = items.order_by('-create_date', '-vote')

        if cur_category:
            # 如果有当前分类
            if cur_category.parent:
                # 如果当前节点有父节点
                category_first = cur_category.parent
                category_second = cur_category
                category_second_items = Category.objects.filter(parent=cur_category.parent)
            else:
                category_first = cur_category
                category_second = None
                category_second_items = Category.objects.filter(parent=cur_category)
        else:
            category_second_items = Category.objects.all()[:12]
        context = {
            'title': 'MindShare',
            'category_first': category_first,
            'category_second': category_second,
            'category_first_items': Category.objects.filter(parent__isnull=True),
            'category_second_items': category_second_items,
            'pages': get_pages(items, cur_page=page, url_generator=index_url_generator, category=category),
            'category': category,
            'order': order
        }

        return render(request, 'mindmap/index.html', context=context)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return return_404_page(request)
