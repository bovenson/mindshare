#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: views_pagination.py
DATE: 17-7-31 下午12:25
DESC: 
"""
import traceback

from django.core.paginator import Paginator

from mindshare.settings import COUNT_PER_PAGE


class PageItem():
    def __init__(self, url='javascript: void(0)', number=1, text=None, active=True):
        self.url = url
        self.number = number
        self.text = text if text is not None else number
        self.active = active


class PageInstance():
    def __init__(self, total_page_number, cur_page_number, cur_page_items, url_generator=None, **kwargs):
        # 所有分页
        self.total_page_number = total_page_number
        # 当前分页
        self.cur_page_number = cur_page_number
        # 当前分页记录
        self.cur_page_items = cur_page_items
        # url 生成器
        self.url_generator = url_generator
        self.kwargs = kwargs
        # 分页列表项目
        self.page_items = []
        self.init_page_items()

    def init_page_items(self):
        _page_items_number = {1, self.total_page_number}
        for i in range(max(1, self.cur_page_number-3), min(self.cur_page_number+3, self.total_page_number)):
            _page_items_number.add(i)
        for page_number in _page_items_number:
            if len(self.page_items) > 0 and self.page_items[-1].number and page_number - self.page_items[-1].number > 1:
                self.page_items.append(PageItem(text='...', active=False))

            if page_number == self.cur_page_number:
                self.page_items.append(PageItem(number=page_number, active=False))
            elif self.url_generator:
                self.page_items.append(PageItem(url=self.url_generator(page_number, **self.kwargs), number=page_number))
            else:
                self.page_items.append(PageItem(number=page_number))


def get_pages(query_set, cur_page=1, count_per_page=COUNT_PER_PAGE, url_generator=None, **kwargs):
    """
    获取供模板使用的分页信息
    :param url_generator:
    :param query_set: model query set
    :param cur_page: 当前页码
    :param count_per_page: 每页记录数
    :return:
    """
    try:
        cur_page = int(cur_page) if cur_page else 1
        page_list = Paginator(query_set, count_per_page)
        total_page_number = page_list.num_pages
        cur_page_number = max(0, min(cur_page, total_page_number))
        cur_page_items = page_list.page(cur_page_number)
        return PageInstance(total_page_number, cur_page_number, cur_page_items, url_generator, **kwargs)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return PageInstance(0, 0, None)

