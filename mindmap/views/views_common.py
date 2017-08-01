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
