#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_category.py
DATE: 17-7-28 下午12:21
DESC: 
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mindmap.models import Category


@csrf_exempt
def show_category(request):
    """获取所有分类"""
    return JsonResponse({'categorys': [v.convert_to_dict() for v in Category.objects.all()]})
