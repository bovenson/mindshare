#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: url_generator.py
DATE: 17-7-31 下午5:07
DESC: 
"""
from django.urls import reverse


def index_url_generator(page=1, category=None, **kwargs):
    if category is not None:
        return reverse('mindmap:index-with-category', args=(category, page))
    else:
        return reverse('mindmap:index-without-category', args=(page, ))


def user_page_pagination_url_generator(page=1, uid=None, *args, **kwargs):
    if uid is not None:
        return reverse('mindmap:user-page', args=(page,))
    else:
        return reverse('mindmap:user-page-with-uid', args=(uid, page))
