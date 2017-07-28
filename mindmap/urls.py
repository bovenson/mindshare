# coding: utf-8
from django.conf.urls import url
from mindmap.views import views_common, views_index, views_mind, views_category


urlpatterns = [
    url(r'^$', views_index.index, name='index'),

    # Mind
    url(r'new-mind-page/?', views_mind.mind_new, name='new-mind-page'),
    url(r'new-mind/?', views_mind.process_new_mind, name='new-mind'),
    url(r'mind/show/(?P<tid>\d+)?/?', views_mind.show_mind_detail, name='show-mind'),
]

# 分类
urlpatterns += [
    url(r'category/show/?', views_category.show_category, name='category-show'),
]

urlpatterns += [
    # 如果都没有匹配, 返回404页面
    url(r'', views_common.return_404_page, name='404-page'),
]