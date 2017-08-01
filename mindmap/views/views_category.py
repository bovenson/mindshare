#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_category.py
DATE: 17-7-28 下午12:21
DESC: 
"""
import traceback

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mindmap.models import Category, MindMap
from mindmap.views.views_common import return_404_page


@csrf_exempt
def show_category(request):
    """获取所有分类"""
    return JsonResponse({'categorys': [v.convert_to_dict() for v in Category.objects.all()]})


# def show_category_page(request, cid):
#     try:
#         category = Category.objects.filter(id=cid).first()
#         items = MindMap.objects.filter(category_id=cid).order_by('-vote')
#
#         context = {
#             'title': '分类 - ' + category.title
#         }
#     except Exception as e:
#         print(e)
#         traceback.print_exc()
#     return return_404_page(request)

