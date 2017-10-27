#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_feedback.py
DATE: 17-10-26 上午9:04
DESC: 用户反馈视图
"""
import traceback

from django.http import JsonResponse

from mindmap.models import FeedbackMessage
from mindmap.views.views_common import json_res


def feedback_add(request):
    """添加反馈
    POST 方法，Json格式
    POST 内容：
        content: 反馈内容
    """
    try:
        # feedback = FeedbackMessage(content=request.POST.get('content'),
        #                            user_id=request.user.id if request.user.is_authenticated() else None)
        feedback = FeedbackMessage(content=request.POST.get('content'),
                                   user=request.user if request.user.is_authenticated() else None)
        feedback.save()
        return JsonResponse(json_res(res=True))
    except Exception as e:
        print(e)
        traceback.print_exc()
        return JsonResponse(json_res(res=False, msg=str(e)))
