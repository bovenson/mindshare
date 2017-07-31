# coding: utf-8
from django.conf.urls import url
from mindmap.views import views_common, views_index, views_mind, views_category, views_user


urlpatterns = [
    url(r'^$', views_index.index, name='index'),
    url(r'^page/(?P<page>\d+)?$', views_index.index, name='index-without-category'),
    url(r'^category/(?P<category>\d+)/page/(?P<page>\d+)?$', views_index.index, name='index-with-category'),

    # Mind
    url(r'new-mind-page/?', views_mind.mind_new, name='new-mind-page'),
    url(r'new-mind/?', views_mind.process_new_mind, name='new-mind'),
    url(r'mind/show/(?P<tid>\d+)?/?', views_mind.show_mind_detail, name='show-mind'),
]

# 分类
urlpatterns += [
    url(r'category/show/?', views_category.show_category, name='category-show'),
]

# 用户相关url
urlpatterns += [
    # 用户书单列表
    url(r'^user/register/?$', views_user.user_register, name='register'),
    url(r'^user/login/?$', views_user.user_login, name='login'),
    url(r'^user/logout/?$', views_user.user_logout, name='logout'),
    url(r'^user/profile/?$', views_user.user_profile, name='user-profile'),
    url(r'^user/profile/update/?$', views_user.user_profile_update, name='user-profile-update'),
    url(r'^user/page/(?P<page>\d+)/?$', views_user.user_page, name='user-page'),
    url(r'^user/(?P<uid>\d+)/page/(?P<page>\d+)/?$', views_user.user_page, name='user-page-with-uid')
]

# 最后
urlpatterns += [
    # 如果都没有匹配, 返回404页面
    url(r'', views_common.return_404_page, name='404-page'),
]

