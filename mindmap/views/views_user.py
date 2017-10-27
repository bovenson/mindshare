# coding: utf-8
# File: user_views.py
# Intro: 用户相关views
# Author: szhkai@qq.com
import traceback

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from mindmap.forms import UserForm, UserUpdateForm
from mindmap.models import MindMap
from mindmap.util.request_util import get_ip_from_request
from mindmap.views.url_generator import user_page_pagination_url_generator
from mindmap.views.views_common import return_404_page, json_res
from mindmap.views.views_pagination import get_pages


def user_register(request):
    """用户注册"""
    res = {
        "res": "error",
        "msg": "未知错误",
    }

    if request.method == "POST":
        # 使用POST的数据新建用户Form
        form = UserForm(request.POST, {'register_ip': get_ip_from_request(request)})
        # 验证是否输入合法
        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.nickname = username
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

            res["res"] = "success"
            res["msg"] = "注册成功"
        else:
            # print(form.errors)
            _msg = ""
            for k, v in form.errors.items():
                _msg += v + ' '
            res["res"] = "error"
            res["msg"] = _msg

    return JsonResponse(res)


def user_login(request):
    """用户登录"""
    res = {
        "res": "error",
        "msg": "未知错误",
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                res["res"] = "success"
                res["msg"] = ""
        else:
            res["res"] = "error"
            res["msg"] = "用户名/密码错误"

    return JsonResponse(res)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def user_page(request, uid=None, page=1):
    try:
        if uid is None:
            uid = request.user.id
        if uid is None:
            return return_404_page(request)
        items = MindMap.objects.filter(public=True, author=uid)
        context = {
            'title': '个人中心',
            'pages': get_pages(items, cur_page=page, url_generator=user_page_pagination_url_generator, uid=uid),
            'user': User.objects.filter(id=uid).first(),
        }

        return render(request, 'mindmap/user-page.html', context)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return return_404_page(request)


def user_profile(request):
    try:
        context = {
            'title': '设置',
        }

        return render(request, 'mindmap/user-profile.html', context)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return return_404_page(request)


@login_required
def user_profile_update(request):
    try:
        # print(request.POST)
        form = UserUpdateForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse(json_res(res=True))
        else:
            # 验证失败
            # 获取错误信息
            msg = [(k, v[0]) for k, v in form.errors.items()]
            return JsonResponse(json_res(res=False, msg=msg))
    except Exception as e:
        print(e)
        traceback.print_exc()
    return JsonResponse(json_res(res=False, msg='未知错误'))
