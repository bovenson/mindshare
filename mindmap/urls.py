# coding: utf-8
from django.conf.urls import url
from mindmap.views import views_common, views_index, views_mind

urlpatterns = [
    url(r'^$', views_index.index, name='index'),
    url(r'new-mind', views_mind.mind_new, name='new-mind'),
]

urlpatterns += [
    # 如果都没有匹配, 返回404页面
    url(r'', views_common.return_404_page, name='404-page'),
]