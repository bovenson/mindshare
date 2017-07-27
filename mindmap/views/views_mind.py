#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_mind.py
DATE: 17-7-27 下午5:44
DESC: 
"""
from django.http import JsonResponse
from django.shortcuts import render


def mind_new(request):
    context = {
        'title': '新建',
    }

    return render(request, 'mindmap/mind-new.html', context=context)


def process_new_mind(request):
    res = {
        'res': 'error',
        'msg': '未知错误',
    }
    try:
        print(request.POST)
        print(request.FILES)
    except Exception as e:
        print(e)
    return JsonResponse(res)
