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


def return_404_page(request, *args, **kwargs):
    return render(request, 'mindmap/404page.html')

