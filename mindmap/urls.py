# coding: utf-8
from django.conf.urls import url
from mindmap import views

urlpatterns = [
]

urlpatterns += [
    # 如果都没有匹配, 返回404页面
    url(r'', views.return_404_page, name='404-page'),
    # url(r'^scrapy$', views.scrapy, name='scrapy'),
]