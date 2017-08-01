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
import traceback

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from mindmap.forms import MindMapForm
from mindmap.models import Category, Tag, MindMap, MindMapVote
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
                        tag = str(tag).strip()
                        if len(tag) == 0:
                            continue
                        tag_instance = Tag.objects.filter(title=tag).first()
                        if not tag_instance:
                            tag_instance = Tag(title=tag)
                        tag_instance.cnt += 1
                        tag_instance.save()

                        instance.tags.add(tag_instance)
            except Exception as e:
                print(e)
                traceback.print_exc()
            return JsonResponse(json_res(res=True))
        else:
            # 验证失败
            # 获取错误信息
            msg = [(k, v[0]) for k, v in form.errors.items()]
            return JsonResponse(json_res(res=False, msg=msg))
    except Exception as e:
        print(e)
        traceback.print_exc()
    return JsonResponse(json_res())


def show_mind_detail(request, tid=None):
    try:
        if tid:
            context = {}
            mindmap = MindMap.objects.filter(id=tid).first()
            if mindmap:
                if MindMapVote.objects.filter(mindmap=mindmap, author=request.user).first() is None:
                    context['voted'] = False
                else:
                    context['voted'] = True
                context['title'] = mindmap.title
                context['mindmap'] = mindmap
                return render(request, 'mindmap/mind-detail.html', context=context)
    except Exception as e:
        print(e)
    return return_404_page(request)


@login_required
@require_http_methods(["POST"])
def delete_mind(request):
    try:
        mindmap_id = request.POST.get('id')
        mindmap = MindMap.objects.filter(id=mindmap_id, public=True).first()
        if mindmap is not None:
            if mindmap.author != request.user and not request.user.is_superuser:
                return JsonResponse(json_res(res=False, msg='不是该导图创建用户无法删除'))
            else:
                mindmap.public = False
                mindmap.save()
                return JsonResponse(json_res(res=True))
        else:
            return JsonResponse(json_res(res=False, msg='思维导图不存在'))
    except Exception as e:
        print(e)
        traceback.print_exc()
    return JsonResponse(json_res(res=False, msg='未知错误'))


@require_http_methods(["POST"])
def mind_vote(request):
    try:
        mindmap_id = request.POST.get('id')
        mindmap = MindMap.objects.filter(id=mindmap_id, public=True).first()
        if mindmap is not None:
            if not request.user.is_authenticated:
                return JsonResponse(json_res(res=False, msg='未登录', action='login'))
            else:
                mindmap_vote = MindMapVote.objects.filter(author=request.user, mindmap=mindmap).first()
                print(mindmap_vote)
                if mindmap_vote is not None:
                    mindmap_vote.delete()
                    mindmap.vote -= max(0, mindmap.vote)
                    mindmap.save()
                    return JsonResponse(json_res(res=True, action='devote', vote=mindmap.vote))
                else:
                    mindmap_vote = MindMapVote(author=request.user, mindmap=mindmap)
                    mindmap_vote.save()
                    mindmap.vote += 1
                    mindmap.save()
                    return JsonResponse(json_res(res=True, action='vote', vote=mindmap.vote))
        else:
            return JsonResponse(json_res(res=False, msg='思维导图不存在'))
    except Exception as e:
        print(e)
        traceback.print_exc()
    return JsonResponse(json_res(res=False, msg='未知错误'))
