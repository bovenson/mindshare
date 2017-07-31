#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_mind.py
DATE: 17-7-27 下午5:44
DESC: 
"""
import re

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from mindmap.forms import MindMapForm
from mindmap.models import Category, Tag, MindMap
from mindmap.views.views_common import json_res, return_404_page


def mind_new(request):
    context = {
        'title': '创建主题',
        'category_first': Category.objects.filter(parent__isnull=True)
    }
    return render(request, 'mindmap/mind-new.html', context=context)


@login_required
def process_new_mind(request):
    try:
        form = MindMapForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # 验证成功
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            # 处理信息
            try:
                # 添加标签
                tags_str = request.POST.get('tags')
                if tags_str:
                    tags = re.split(r'[,，]', tags_str)
                    for tag in tags:
                        tag_instance = Tag.objects.filter(title=tag)
                        if not tag_instance:
                            tag_instance = Tag(title=tag)
                        tag_instance.count += 1
                        tag_instance.save()

                        instance.tags.add(tag_instance)
            except Exception as e:
                print(e)
            return JsonResponse(json_res(res=True))
        else:
            # 验证失败
            # 获取错误信息
            msg = [(k, v[0]) for k, v in form.errors.items()]
            return JsonResponse(json_res(res=False, msg=msg))
    except Exception as e:
        print(e)
    return JsonResponse(json_res())


def show_mind_detail(request, tid=None):
    try:
        if tid:
            context = {}
            mindmap = MindMap.objects.filter(id=tid).first()
            if mindmap:
                context['title'] = mindmap.title
                context['mindmap'] = mindmap
                return render(request, 'mindmap/mind-detail.html', context=context)
    except Exception as e:
        print(e)
    return return_404_page(request)
