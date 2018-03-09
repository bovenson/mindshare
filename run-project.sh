#!/usr/bin/env bash
/usr/bin/python3 manage.py runserver 0.0.0.0:9000 1>./other/log/stdout.log 2>./other/log/stderr.log &