#!/bin/bash
/usr/bin/python3 ../../manage.py migrate
/usr/bin/python3 ../../manage.py makemigrations
/usr/bin/python3 ../../manage.py migrate mindmap
/usr/bin/python3 ../../manage.py makemigrations mindmap
