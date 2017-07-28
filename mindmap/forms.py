#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: forms.py
DATE: 17-7-28 上午9:48
DESC: 
"""
from django.core.files.uploadedfile import InMemoryUploadedFile

from mindmap.models import *
from django import forms

from mindshare.limites import UPLOAD_IMG_FORMAT, UPLOAD_IMG_MAX_SIZE, UPLOAD_MINDMAP_FORMAT, UPLOAD_MINDMAP_MAX_SIZE


class MindMapForm(forms.ModelForm):
    class Meta:
        model = MindMap
        fields = ['title', 'description', 'img', 'mindmap', 'share', 'category']

    def clean_img(self):
        _res = ''
        data = self.cleaned_data['img']
        if data:
            if str(data.name).split('.')[-1].lower() not in UPLOAD_IMG_FORMAT:
                _res += '图片格式不允许.'

            if data.size > UPLOAD_IMG_MAX_SIZE * 1024 * 1024:
                _res += '图片过大, 请上传小于 %dMB 大小的图片.' % UPLOAD_IMG_MAX_SIZE

        else:
            _res += '您必须上传图片.'
        if len(_res) > 0:
            raise forms.ValidationError(_res)
        return data

    def clean_mindmap(self):
        _res = ''
        data = self.cleaned_data['mindmap']
        if data:
            if str(data.name).split('.')[-1].lower() not in UPLOAD_MINDMAP_FORMAT:
                _res += '文件格式不允许.'

            if data.size > UPLOAD_IMG_MAX_SIZE * 1024 * 1024:
                _res += '文件过大, 请上传小于 %dMB 大小的文件.' % UPLOAD_MINDMAP_MAX_SIZE

            if len(_res) > 0:
                raise forms.ValidationError(_res)
        return data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'nickname']
