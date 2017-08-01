#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: forms.py
DATE: 17-7-28 上午9:48
DESC: 
"""
from django.contrib.auth import authenticate
from django.core.files.uploadedfile import InMemoryUploadedFile

from mindmap.models import *
from django import forms

from mindshare.limites import UPLOAD_IMG_FORMAT, UPLOAD_IMG_MAX_SIZE, UPLOAD_MINDMAP_FORMAT, UPLOAD_MINDMAP_MAX_SIZE


class MindMapForm(forms.ModelForm):
    categoryFirst = forms.IntegerField()
    img = forms.ImageField(required=False)

    class Meta:
        model = MindMap
        fields = ['title', 'description', 'mindmap', 'share', 'category']

    def clean(self):
        cleaned_data = super(MindMapForm, self).clean()
        category_first = cleaned_data.get('categoryFirst')
        category = cleaned_data.get('category')
        if category is None:
            cleaned_data['category'] = Category.objects.filter(id=category_first).first()

    def clean_img(self):
        _res = ''
        data = self.cleaned_data['img']
        if data:
            if str(data.name).split('.')[-1].lower() not in UPLOAD_IMG_FORMAT:
                _res += '图片格式不允许.'

            if data.size > UPLOAD_IMG_MAX_SIZE * 1024 * 1024:
                _res += '图片过大, 请上传小于 %dMB 大小的图片.' % UPLOAD_IMG_MAX_SIZE

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
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'nickname']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')
        new_password_repeat = cleaned_data.get('new_password_repeat')

        if password and len(password) > 0:
            if new_password and len(new_password) > 0:
                if new_password != new_password_repeat:
                    self.add_error('password', '两次输入的新密码不一致')
                elif len(new_password) < 5:
                    self.add_error('password', '密码不要小于5位')

    def clean_nickname(self):
        data = self.cleaned_data['nickname']
        if 4 < len(data) <= 35:
            return data
        else:
            raise forms.ValidationError('昵称/邮箱 长度为5-35位')


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password_repeat = forms.CharField(widget=forms.PasswordInput, required=False)
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['nickname']

    def clean(self):
        cleaned_data = super(UserUpdateForm, self).clean()
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')
        new_password_repeat = cleaned_data.get('new_password_repeat')

        if password and len(password) > 0:
            if new_password and len(new_password) > 0:
                user = authenticate(username=self.instance.username, password=password)
                if user is None:
                    self.add_error('password', '密码输入错误')
                if new_password != new_password_repeat:
                    self.add_error('password', '两次输入的新密码不一致')
                elif len(new_password) < 5:
                    self.add_error('password', '密码不要小于5位')

    def clean_nickname(self):
        data = self.cleaned_data['nickname']
        if 4 < len(data) <= 35:
            return data
        else:
            raise forms.ValidationError('昵称/邮箱 长度为5-35位')

    def save(self, commit=True):
        # 重写save方法
        instance = super(UserUpdateForm, self).save(commit=False)

        # 修改密码
        cleaned_data = super(UserUpdateForm, self).clean()
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')
        if len(password) > 0:
            # 密码
            if len(new_password) > 0:
                instance.set_password(new_password)

        if commit:
            instance.save()
        return instance
