#!/usr/bin python3
# coding: utf-8

"""
AUTHOR: bovenson
EMAIL: szhkai@qq.com
FILE: request_util.py
DATE: 17-10-26 上午11:22
DESC: 
"""


def get_ip_from_request(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]
    else:
        client_ip = request.META['REMOTE_ADDR']
    return client_ip
