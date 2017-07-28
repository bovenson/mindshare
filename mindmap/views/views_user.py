# coding: utf-8
# File: user_views.py
# Intro: 用户相关views
# Author: szhkai@qq.com

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect

from mindmap.forms import UserForm


def user_register(request):
    """用户注册"""
    res = {
        "res": "error",
        "msg": "未知错误",
    }

    if request.method == "POST":
        # 使用POST的数据新建用户Form
        form = UserForm(request.POST)
        # 验证是否输入合法
        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

            res["res"] = "success"
            res["msg"] = "注册成功"
        else:
            res["res"] = "error"
            res["msg"] = "用户已存在/信息输入不符合格式"

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


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
