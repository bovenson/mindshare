#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_common.py
DATE: 17-7-27 下午12:29
DESC: 
"""
from django.shortcuts import render

from mindmap.models import Article


def return_404_page(request):
    return render(request, 'mindmap/404page.html')


def json_res(res=False, msg=None, data=None, **kwargs):
    res_dict = {
        'res': 'success' if res else 'error',
        'msg': '操作成功' if res else '未知错误',
        'data': data
    }
    res_dict.update(kwargs)

    if msg:
        res_dict['msg'] = msg
    return res_dict


def about_view(request):
    article = Article.objects.filter(title='about').first() or Article.objects.filter(title='关于').first()    # 获取

    context = {
        'title': '关于',
        'article': article
    }

    return render(request, 'mindmap/html/markdown-show.html', context=context)
