#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-5 下午3:12'


import threading

def hello():
    print('hello wrold')

t = threading.Timer(5,hello)
t.start()
