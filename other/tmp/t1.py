#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: t1.py
DATE: 17-8-1 上午10:20
DESC: 
"""


def fa(*args, **kwargs):
    d_ = {'cc': 98}
    print(args)
    print(kwargs)
    d_.update(kwargs)
    print(d_)
    print(*args)


fa(3, 4, a=1, b=2)


